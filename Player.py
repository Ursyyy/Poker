class Player:
    
    def __init__(self, money):
        self._money = money
        self._hand = []

    def StrHand(self):
        return str(self._hand[0]) + " " + str(self._hand[1])

    def TakeACard(self, card):
        self._hand.append(card)            

    def ChangeMoney(self, money):
        self._money -= money

    def Money(self):
        return self._money

    def Hand(self):
        return self._hand

