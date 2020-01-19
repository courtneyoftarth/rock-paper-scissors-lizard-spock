class Move:
    count = 0

    def __init__(self, name):
        self.__name = name
        self.__beats = []

        Move.count += 1
        self.__id = Move.count
    
    def addBeats(self, *others):
        for other in others:
            self.__beats.append(other.__id)

    def isWinner(self, other):
        return other.__id in self.__beats

    def getId(self):
        return self.__id

    def getSerialized(self):
        return {
            "id": self.__id,
            "name": self.__name
        }
