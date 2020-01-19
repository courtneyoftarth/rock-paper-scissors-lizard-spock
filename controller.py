from flask import Flask, jsonify, request
from flask_cors import CORS
from data.choices import getChoice, getChoices
from data.play import playMove


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "https://codechallenge.boohma.com"}})

@app.route("/choice")
def choice():
    data = getChoice()
    return jsonify(data)

@app.route("/choices")
def choices():
    data = getChoices()
    return jsonify(data)

@app.route("/play", methods = ["POST"])
def play():
    data = playMove(request.json['player'])
    return jsonify(data)

if __name__ == "__main__":
    app.run()