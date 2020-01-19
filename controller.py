from flask import Flask, jsonify
from flask_cors import CORS
from data.choices import getChoice, getChoices
from data.play import playMove


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

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
    data = playMove()
    return jsonify(data)

if __name__ == "__main__":
    app.run()