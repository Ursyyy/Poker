from Card import Card

class Deck:

    def __init__ (self):
        self.__deck = []
        for rank in Card.RANK:
            for suit in Card.SUIT:
                self.__deck.append(Card (suit, rank))

    def Shuffle(self):
        from random import shuffle
        shuffle(self.__deck)

    def Deal (self):
        if len(self.__deck) == 0:
            return None
        else:
            return self.__deck.pop(0)