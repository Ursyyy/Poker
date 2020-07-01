from Player import Player

class Computer(Player):

    def Bet(self):
        from random import randint
        bet = randint(1,20) * 20
        self.ChangeMoney(bet)
        return bet
  