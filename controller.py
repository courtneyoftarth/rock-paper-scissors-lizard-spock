from flask import abort, Flask, jsonify, request
from flask_cors import CORS
from data.game import Game


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "https://codechallenge.boohma.com"}})

game = Game()

@app.route("/choice")
def choice():
    move = game.getRandomMove()
    return jsonify(move.getSerialized())

@app.route("/choices")
def choices():
    moves = game.getAllMoves()
    return jsonify([move.getSerialized() for move in moves])

@app.route("/play", methods = ["POST"])
def play():
    if (request.json is None or request.json['player'] is None):
        abort(400, "Expected parameter player")
    
    moveId = request.json['player']
    if (not game.hasMove(moveId)):
        abort(400, "Parameter player is not a valid move id")

    playerMove = game.getMove(moveId)
    computerMove = game.getRandomMove()

    return jsonify({
        "computer": computerMove.getId(),
        "player": playerMove.getId(),
        "results": "win" if playerMove.isWinner(computerMove) else "lose" if computerMove.isWinner(playerMove) else "tie" 
    })

if __name__ == "__main__":
    app.run()