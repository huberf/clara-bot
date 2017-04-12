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

@app.route("/converse", methods=['POST'])
def parse_request():
    text = json.dumps(request.json)
    message = request.json["input"]
    message = message.lower()
    response = brain.get_response(message)
    if not response == None:
        return response
    else:
        return "Sorry! I'm still learning to understanding."
    # Legacy Tests kept for future difficulties
    '''
    return 'JSON Message: ' + json.dumps(request.json)
    return request.args['input']
    starter = request.json
    return json.dumps(starter)
    message = starter['input']
    return 'Hey: ' + brain.get_response(message)
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 2525))
    app.run(host='0.0.0.0', port=port, debug=True)
