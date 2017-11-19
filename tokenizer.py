'''''''
Tokenizing for context inspired by https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077
'''''''

from utils import convo_reader
import json
from os import listdir
import hashlib

# things we need for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf
import random

# import our chat-bot intents file
'''
import json
with open('intents.json') as json_data:
    intents = json.load(json_data)
'''

# Append all conversation response around distributed conversation files
# This allows one to "plug-in" new responses and have them centralized together
convo = []
data = {'convo_dir': 'convos/'}
convoFiles = listdir(data['convo_dir'])
for i in convoFiles:
    if i.endswith('.json'):
        convoFile = open('convos/' + i)
        raw_data = convoFile.read()
        convo += json.loads(raw_data)
    elif i.endswith('.convo'):
        # Process the loose file format
        convoFile = open('convos/' + i)
        raw_data = convoFile.read()
        convo += convo_reader.convert_to_json(raw_data)

tagged = []
for i in convo:
    tag = ""
    message = ""
    for a in i['starters']:
        message += a + ';'
    m = hashlib.md5()
    m.update(message.encode("utf-8"))
    tag = str(m.digest())
    i['tag'] = tag
    tagged += [i]
convo = tagged


words = []
classes = []
documents = []
ignore_words = ['?']
# loop through each sentence in our intents patterns
for intent in convo:
    for pattern in intent['starters']:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern)
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# remove duplicates
classes = sorted(list(set(classes)))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)
