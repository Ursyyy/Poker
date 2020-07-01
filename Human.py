from Player import Player

class Human(Player):
   
    def Bet (self):
        money = int(input("Input your bet: "))
        self.ChangeMoney(money)
        return money
