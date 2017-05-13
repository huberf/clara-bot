from random import randint
from Levenshtein import distance
from os import listdir
import json

# Config load
configFile = open('config.json')
raw_data = configFile.read()
data = json.loads(raw_data)

# Emotion load
emotionFile = open('emotions.json')
raw_data = emotionFile.read()
emotions = json.loads(raw_data)
emotionFile.close()

# Append all conversation response around distributed conversation files
# This allows one to "plug-in" new responses and have them centralized together
convo = []
convoFiles = listdir('convos/')
for i in convoFiles:
    if i.endswith('.json'):
        convoFile = open('convos/' + i)
        raw_data = convoFile.read()
        convo += json.loads(raw_data)

# Var Setup
VAR_REGISTRY = {}
def build_registry():
    global VAR_REGISTRY
    VAR_REGISTRY = {
            "user_name": data['user']['name'],
            "name": data['name'],
            "response_count": len(convo),
            "user_hobby": data['user']['hobby'],
            "happy_level": emotions['happy'],
            "stress_level": emotions['stress'],
            "animosity": emotions['animosity']
            }

build_registry()

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
                reply_options = []
                for b in i['replies']:
                    try:
                        to_test = b['qualifiers']
                        for z in to_test:
                            if VAR_REGISTRY[z['name']] == z['val']:
                                reply_options += [b['text']]
                            else:
                                do_nothing = True
                    except:
                        reply_options += [b['text']]
                slimmed_reply = reply_options[randint(0, len(reply_options)-1)]
                possibilities.append({'val': val, 'response': slimmed_reply})
    min = 10000000000
    response = 'None'
    # print(possibilities)
    for i in possibilities:
        if i['val'] < min:
            response = i['response']
            min = i['val']
    return response.format(**VAR_REGISTRY)

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
    emotionFile = open('emotions.json', 'w')
    emotionFile.write(json.dumps(emotions))
    emotionFile.close()
