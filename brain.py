from random import randint
import json
configFile = open('config.json')
raw_data = configFile.read()
data = json.loads(raw_data)

convoFile = open('convo.json')
raw_data = convoFile.read()
convo = json.loads(raw_data)

def get_response(input):
    for i in convo:
        for a in i['starters']:
            if input == a:
                response = i['replies'][randint(0, len(i['replies']) - 1)]['text']
                return response.format(
                        user_name=data['user']['name'],
                        name=data['name'],
                        response_count=len(convo)
                        )

if __name__ == "__main__":
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
