from random import choice

class Move:
    count = 0

    def __init__(self, name):
        self.name = name
        self.beats = []

        Move.count += 1
        self.id = Move.count
    
    def addBeats(self, *others):
        for other in others:
            self.beats.append(other.id)

    def isWinner(self, other):
        return other.id in self.beats
