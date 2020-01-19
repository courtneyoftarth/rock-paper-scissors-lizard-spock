from random import choice
from moves import moves

class Score():
    player = 0
    computer = 0

def playMove(moveId):
    playerMove = [move for move in moves if move["id"] == moveId]
    computerMove = choice(moves)

    return {
        "results":"win",
        "player":5,
        "computer":1
    }