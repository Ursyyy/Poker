class Card:
    
    SUIT = ("H", "D", "C", "S")
    RANK = ("A", "K", "Q", "J", "2", "3", "4", "5", "6", "7", "8", "9", "10")

    def __init__ (self, suit, rank):
        self.__suit = suit
        self.__rank = rank       

    def Suit(self):
        return self.__suit
    
    def __str__(self):
        return self.__rank + self.__suit

    def Rank(self):
        if(self.__rank == "A"):
            return 14
        elif(self.__rank == "K"):
            return 13
        elif(self.__rank == "Q"):
            return 12
        elif(self.__rank == "J"):
            return 11
        else:
            return int(self.__rank) 

    def __eq__ (self, other):
        return (self.__rank == other.__rank)

    def __ne__ (self, other):
        return (self.__rank != other.__rank)

    def __lt__ (self, other):
        return (self.__rank < other.__rank)

    def __le__ (self, other):
        return (self.__rank <= other.__rank)

    def __gt__ (self, other):
        return (self.__rank > other.__rank)

    def __ge__ (self, other):
        return (self.__rank >= other.rank)