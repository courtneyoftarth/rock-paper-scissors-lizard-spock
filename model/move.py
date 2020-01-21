# A Move can be compared to another Move or serialized
class Move:
    count = 0

    # Return a new Move with the given name
    def __init__(self, name):
        self.__name = name
        self.__beats = []

        Move.count += 1
        self.__id = Move.count
    
    # Modify this Move such that it can now beat the given other Moves
    def addBeats(self, *others):
        for other in others:
            self.__beats.append(other.__id)

    # Return true if this Move beats the other Move, false otherwise.
    # It also returns false if there is a tie, because that means this move did not win.
    def isWinner(self, other):
        return other.__id in self.__beats

    # Return the id of this Move
    def getId(self):
        return self.__id

    # Return an object representation of this Move
    def getObjectValue(self):
        return {
            "id": self.__id,
            "name": self.__name
        }
