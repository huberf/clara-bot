import brain
import os
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def main():
    return "Personal Clara instance."

@app.route("/converse", methods=['POST'])
def parse_request():
    starter = request.form['input']
    return brain.get_response(starter)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 2525))
    app.run(host='0.0.0.0', port=port, debug=True)
