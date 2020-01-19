from flask import Flask, jsonify
from flask_cors import CORS
from data.choices import getChoices


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/choices")
def choices():
    data = getChoices()
    return jsonify(data)

if __name__ == "__main__":
    app.run()