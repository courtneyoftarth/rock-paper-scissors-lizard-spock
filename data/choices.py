from random import choice

moves = [
    {
        "id": 1,
        "name": "rock"
    },
    {
        "id": 2,
        "name": "paper"
    },
    {
        "id": 3,
        "name": "scissors"
    },
    {
        "id": 4,
        "name": "lizard"
    },
    {
        "id": 5,
        "name": "spock"
    }
]

def getChoices():
    return moves

def getChoice():
    return choice(moves)