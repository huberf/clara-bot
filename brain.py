from random import randint
from Levenshtein import distance
from os import listdir
import json
configFile = open('config.json')
raw_data = configFile.read()
data = json.loads(raw_data)

# Append all conversation response around distributed conversation files
# This allows one to "plug-in" new responses and have them centralized together
convo = []
convoFiles = listdir('convos/')
for i in convoFiles:
    if i.endswith('.json'):
        convoFile = open('convos/' + i)
        raw_data = convoFile.read()
        convo += json.loads(raw_data)

def punctuation_stripper(statement):
    toRemove = ['.', '!', '?']
    punctuate = None
    for i in toRemove:
        if not statement.find(i) == -1:
            punctuate = i
        statement = statement.strip(i)
    return {"text": statement, "punctuation": punctuate}

def get_response(input):
    # Remove currently useless characters
    stripped = punctuation_stripper(input)
    input = stripped["text"]
    punctuation = stripped["punctuation"]
    possibilities = []
    for i in convo:
        for a in i['starters']:
            val = distance(input, a)
            if len(input)/(val+1) > 1.5:
                possibilities.append({'val': val, 'response': i['replies'][randint(0, len(i['replies']) - 1)]['text']})
    min = 10000000000
    response = 'None'
    print(possibilities)
    for i in possibilities:
        if i['val'] < min:
            response = i['response']
            min = i['val']
    return response.format(
            user_name=data['user']['name'],
            name=data['name'],
            response_count=len(convo),
            user_hobby=data['user']['hobby']
                )

if __name__ == "__main__":
    logFile = open('log.txt', 'a')
    print("Booting...")
    print("{} online.".format(data['name']))
    statement = ""
    while statement != "quit":
        statement = input("> ")
        response = get_response(statement.lower())
        print(response)
        ender = '\n'
        logFile.write('S: ' + statement + ender)
        if not response == None:
            logFile.write('R: ' + response + ender)
        else:
            logFile.write('R: None' + ender)
