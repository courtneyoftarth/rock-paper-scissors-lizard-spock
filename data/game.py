from random import choice
from move import Move

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

    def getAllMoves(self):
        return self.__movesMap.values()

    def getRandomMove(self):
        return choice(self.__movesMap.values())

    def getMove(self, id):
        return self.__movesMap[id]

    def hasMove(self, id):
        return id in self.__movesMap