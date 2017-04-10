from random import randint
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

def get_response(input):
    for i in convo:
        for a in i['starters']:
            if input == a:
                response = i['replies'][randint(0, len(i['replies']) - 1)]['text']
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
        # Strip currently useless characters
        statement = statement.strip('.')
        statement = statement.strip('!')
        response = get_response(statement.lower())
        print(response)
        ender = '\n'
        logFile.write('S: ' + statement + ender)
        if not response == None:
            logFile.write('R: ' + response + ender)
        else:
            logFile.write('R: None' + ender)
