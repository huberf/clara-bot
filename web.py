import brain
import os
from flask import json
from flask import jsonify
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def main():
    return "Personal Clara instance."

def log(text, response):
    logFile = open('log.txt', 'a')
    ender = '\n'
    logFile.write('S: ' + text + ender)
    if not response == None:
        logFile.write('R: ' + response + ender)
    else:
        logFile.write('R: None' + ender)

@app.route("/converse", methods=['POST'])
def parse_request():
    try:
        text = json.dumps(request.json)
        message = request.json['input']
    except:
        message = request.form['input']
    message = message.lower()
    response = brain.get_response(message)
    # Logging i/o
    if not response == None:
        log(message, response['message'])
    else:
        log(message, None)
    if not response == None:
       to_return = '{"message": "' + response['message'] + '", "image": "' + response['image'] + '"}'
       return to_return
    else:
        return '{"message": "' + "Sorry! I'm still learning to understanding." + '"}'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 2525))
    app.run(host='0.0.0.0', port=port, debug=True)
