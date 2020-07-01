from Deck import Deck
from Human import Human
from Computer import Computer

from os import system

class Poker:

    def __init__(self):
        self.__human = Human(1200)
        self.__computer = Computer(1200)
        self.__bet = 0
        self.__table = []

    def NewGame(self):
        from time import sleep
        cont = 1
        while self.__computer.Money() > 0 and self.__human.Money() > 0  and cont == 1:
            system("CLS")
            __bet = 0
            deck = Deck()
            deck.Shuffle()
            for _ in range(2):
                self.__human.TakeACard(deck.Deal())
                self.__computer.TakeACard(deck.Deal())
            for _ in range(3):
                self.__table.append(deck.Deal())            
            self.__PrintTheGame__()
            sleep(4)
            self.__Bet__()
            system("CLS")
            self.__table.append(deck.Deal())
            self.__PrintTheGame__()
            sleep(4)
            self.__Bet__()
            system("CLS")
            self.__table.append(deck.Deal())
            self.__PrintTheGame__()
            sleep(4)
            self.__Bet__()
            system("CLS")
            sleep(6)
            self.__Winner__()
            sleep(3)
            system("CLS")
            cont = int(input("Continue?(1 - yes/0 - no): "))
        
    def __PrintTheGame__(self):
        print("Your opponent’s money: " + str(self.__computer.Money()) + "\n")
        print("Table: ", end=" ")
        for card in self.__table:
            print(card, end=" ")
        print("\n")
        print("Your's money: " + str(self.__human.Money()))
        print("Your's hand: " + self.__human.StrHand())

    def __Bet__(self):
        humanBet = self.__human.Bet()
        if humanBet == 0:
            self.__computer.ChangeMoney(-self.__bet)
        computerBet = self.__computer.Bet()
        if computerBet > humanBet:
            diff = computerBet - humanBet
            choise = int(input("Your's opponent bet is more on {0}\nCall?(1 - yes/ 0 - no): ".format(diff)))
            if choise == 1:
                humanBet = computerBet
                self.__human.ChangeMoney(diff)
        else:
            from random import randint
            if randint(1, 11) % 11 == 0:
                computerBet = humanBet
                self.__computer.ChangeMoney(computerBet - humanBet)
        self.__bet = humanBet + computerBet

    def __Winner__(self):
        sortedHumanHand = sorted(self.__human.Hand() + self.__table)
        sortedCompHand = sorted(self.__computer.Hand() + self.__table)
        if self.__RoyalFlush__(sortedHumanHand):
            self.__human.ChangeMoney(-self.__bet)
            print("You're win!\nYou have a Royal Flush!!")
        elif self.__RoyalFlush__(sortedCompHand):
            self.__computer.ChangeMoney(-1*self.__bet)
            print("Your's opponent are win\nYour opponent has a Royal Flush!!")
        elif self.__StraightFlush__(sortedHumanHand):
            self.__human.ChangeMoney(-1*self.__bet)
            print("You're win!nYou have a Straight Flush")
        elif self.__StraightFlush__(sortedCompHand):
            self.__computer.ChangeMoney(-1*self.__bet)
            print("Your's opponent are win\nYour opponent has a Straight Flush")
        elif self.__FourOfAKind__(sortedHumanHand):
            self.__human.ChangeMoney(-1*self.__bet)
            print("You're win!\nYou have a Four of a kind")
        elif self.__FourOfAKind__(sortedCompHand):
            self.__computer.ChangeMoney(-1*self.__bet)
            print("Your's opponent are win\nYour opponent has a Four of a kind")
        elif self.__FullHouse__(sortedHumanHand):
            self.__human.ChangeMoney(-1*self.__bet)
            print("You're win!\nYou have a Full House")
        elif self.__FullHouse__(sortedCompHand):
            self.__computer.ChangeMoney(-1*self.__bet)
            print("Your's opponent are win\nYour opponent has a Full House")
        elif self.__Flush__(sortedHumanHand):
            self.__human.ChangeMoney(-1*self.__bet)
            print("You're win!\nYou have a Flush")
        elif self.__Flush__(sortedCompHand):
            self.__computer.ChangeMoney(-1 * self.__bet)
            print("Your's opponent are win\nYour opponent has a Flush")
        elif self.__Straight__(sortedHumanHand):
            self.__human.ChangeMoney(-1*self.__bet)
            print("You're win!\nYou have a Straight")
        elif self.__Straight__(sortedCompHand):
            self.__computer.ChangeMoney(-1*self.__bet)
            print("Your's opponent are win\nYour opponent has a Straight")
        elif self.__Set__(sortedHumanHand):
            self.__human.ChangeMoney(-1*self.__bet)
            print("You're win!\nYou have a Set")
        elif self.__Set__(sortedCompHand):
            self.__computer.ChangeMoney(-1*self.__bet)
            print("Your's opponent are win\nYour opponent has a Set")
        elif self.__TwoPairs__(sortedHumanHand):
            self.__human.ChangeMoney(-1*self.__bet)
            print("You're win!\nYou have two Pairs")
        elif self.__TwoPairs__(sortedCompHand):
            self.__computer.ChangeMoney(-1*self.__bet)
            print("Your's opponent are win\nYour opponent has two Pairs")
        elif self.__Pair__(sortedHumanHand):
            self.__human.ChangeMoney(-1*self.__bet)
            print("You're win!\nYou have a Pair")
        elif self.__Pair__(sortedCompHand):
            self.__computer.ChangeMoney(-1*self.__bet)
            print("Your's opponent are win\nYour opponent has a Pair")
        elif self.__High__(sortedHumanHand) > self.__High__(sortedCompHand):
            self.__human.ChangeMoney(-1*self.__bet)
            print("You're win!\nYou have a high card")
        else:
            self.__computer.ChangeMoney(-1 * self.__bet)
            print("Your's opponent are win\nYour opponent has a high card")
        
            

    def __RoyalFlush__(self, sortedHand):
        firstCardRank = sortedHand[0].Rank()
        firstCardSuit = sortedHand[0].Suit()
        flag = True
        for card in sortedHand:
            if card.Suit() != firstCardSuit or card.Rank() != firstCardRank:
                flag = False
                break
            else:
                firstCardRank += 1
        return flag

    def __StraightFlush__(self, sortedhand):
        return self.__Straight__(sortedhand) and self.__Flush__(sortedhand)

    def __FourOfAKind__(self, sortedHand):
        count = 0
        firstCardRank = sortedHand[0].Rank()
        for card in sortedHand:
            if card.Rank() == firstCardRank:
                count +=1
        if count == 4:
            return True
        return False

    def __FullHouse__(self, sortedHand):
        newSortedHand = sortedHand.copy()
        for card in range(1, len(sortedHand) - 1):
            if sortedHand[card].Rank() == sortedHand[card + 1].Rank() and sortedHand[card].Rank() == sortedHand[card - 1].Rank():
                del newSortedHand[card - 1]
                del newSortedHand[card]
                del newSortedHand[card + 1]
                break
        else:
            return False
        if self.__Pair__(newSortedHand):
            return True
        return False


    def __Flush__(self, sortedHand):
        count = 0
        for card in range(len(sortedHand) - 1):
            if sortedHand[card].Suit() == sortedHand[card + 1].Suit():
                count += 1
        if count == 5:
            return True
        return False

    def __Straight__(self, sortedHand):
        count = 0
        for card in range(len(sortedHand) - 1):
            if sortedHand[card].Rank() == sortedHand[card + 1].Rank() + 1:
                count += 1
        if count == 5:
            return True
        return False

    def __Set__(self, sortedHand):
        for card in range(1, len(sortedHand) - 1):
            if sortedHand[card].Rank() == sortedHand[card + 1].Rank() and sortedHand[card].Rank() == sortedHand[card - 1].Rank():
                return True
        return False

    def __TwoPairs__(self, sortedHand):
        newSortedHand = sortedHand.copy()
        for card in range(len(sortedHand) - 1):
            if sortedHand[card].Rank() == sortedHand[card + 1].Rank():
                del newSortedHand[card]
                del newSortedHand[card + 1]
                break
            else:
                return False
        for card in range(len(newSortedHand) - 1):
            if newSortedHand[card].Rank() == newSortedHand[card + 1].Rank():
                return True
        return False

    def __Pair__(self, sortedHand):
        for card in range(len(sortedHand) - 1):
            if sortedHand[card].Rank() == sortedHand[card + 1].Rank():
                return True
        return False

    def __High__(self, sortedHand):
        high = sortedHand[0].Rank()
        for card in sortedHand:
            if card.Rank() > high:
                high = card.Rank()
        return high 