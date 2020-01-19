from flask import Flask, jsonify, request
from flask_cors import CORS
from data.game import Game


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "https://codechallenge.boohma.com"}})

game = Game()

@app.route("/choice")
def choice():
    move = game.getRandomMove()
    return jsonify(move.__dict__)

@app.route("/choices")
def choices():
    moves = game.getAllMoves()
    return jsonify([move.__dict__ for move in moves])

@app.route("/play", methods = ["POST"])
def play():
    moveId = request.json['player']
    playerMove = game.getMove(moveId)
    computerMove = game.getRandomMove()

    return jsonify({
        "computer": computerMove.id,
        "player": playerMove.id,
        "results": "win" if playerMove.isWinner(computerMove) else "lose" if computerMove.isWinner(playerMove) else "tie" 
    })

if __name__ == "__main__":
    app.run()