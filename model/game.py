import math
from service.random import Random
from .move import Move

# Manages RPSLS state
random = Random()
class Game:
    def __init__(self):
        rock = Move("rock")
        paper = Move("paper")
        scissors = Move("scissors")
        lizard = Move("lizard")
        spock = Move("spock")

        rock.addBeats(scissors, lizard)
        paper.addBeats(rock, spock)
        scissors.addBeats(paper, lizard)
        lizard.addBeats(paper, spock)
        spock.addBeats(rock, scissors)

        self.__movesMap = dict((move.getId(), move) for move in [rock, paper, scissors, lizard, spock])

    # Get all valid Moves 
    # Returns a list of Moves
    def getAllMoves(self):
        return list(self.__movesMap.values())

    # Get a random valid Move
    def getRandomMove(self):
        movesList = list(self.__movesMap.values())
        index = math.floor(random.getRandom() / 100 * len(movesList)) # turn number between 0-100 to 0-len(movesList)
        return movesList[index]

    # Get a Move by id
    def getMove(self, id):
        return self.__movesMap[id]

    # Check whether the given move id is valid
    def hasMove(self, id):
        return id in self.__movesMap