#!/usr/bin/env python3

import random

from Card import Card
from Deck import Deck
from Hand import Hand
from Player import Player
from Randy import Randy
from DeepPreschooler import DeepPreschooler
from Human import Human
from Oddball import Oddball
from Smarty import Smarty


class PreschoolPoker:
    def __init__(self, player1Name, player1Type, player2Name, player2Type, v):
        initialCardsInDeck = [Card(1), Card(2), Card(3), Card(1), Card(2), Card(3), Card(1), Card(2), Card(3)]
        self.deck = Deck(initialCardsInDeck)
        coin = ['H', 'T']
        coinFlip = random.choice(coin)
        self.v = v  # only for the Smarty, I know it's a hack, but I don't have a lot of time for this assignment.
        if coinFlip == 'H':
            self.player1 = self.getPlayer(player1Name, player1Type)
            self.player2 = self.getPlayer(player2Name, player2Type)
        else:
            self.player2 = self.getPlayer(player2Name, player2Type)
            self.player1 = self.getPlayer(player1Name, player1Type)

    def getPlayer(self, playerName, playerType):
        if playerType == 'Randy':
            return Randy(playerName, self.deck)
        elif playerType == 'DeepPreschooler':
            return DeepPreschooler(playerName, self.deck)
        elif playerType == 'Human':
            return Human(playerName, self.deck)
        elif playerType == 'Smarty':
            return Smarty(playerName, self.deck, self.v, 0.5)
        elif playerType == 'Oddball':
            return Oddball(playerName, self.deck)
        else:
            return Player(playerName, self.deck)

    def winnerPlayerNum(self):
        if self.player1.getHandValue() > self.player2.getHandValue():
            return 1  # self.player1
        elif self.player1.getHandValue() < self.player2.getHandValue():
            return 2  # self.player2
        else:
            return None

    def winner(self):
        if self.player1.getHandValue() > self.player2.getHandValue():
            return self.player1
        elif self.player1.getHandValue() < self.player2.getHandValue():
            return self.player2
        else:
            return None

    def getPlayer1(self):
        return self.player1

    def getPlayer2(self):
        return self.player2

    def play(self):
        coin = ['H', 'T']
        coinFlip = random.choice(coin)
        if coinFlip == 'H':
            self.player1.doit(self.deck)
            self.player2.doit(self.deck)
        else:
            self.player2.doit(self.deck)
            self.player1.doit(self.deck)
        print('Winner is: ', self.winner())


def teach(numTrials, opponentName, opponentType):  # here I always want player 2 to be the Smarty
    v = {(1, 1): 0.5,
         (1, 2): 0.5,
         (1, 3): 0.5,
         (2, 2): 0.5,
         (2, 3): 0.5,
         (3, 3): 0.5,
         }
    smartyWins = 0
    otherWins = 0
    for i in range(numTrials):
        preSchoolPoker = PreschoolPoker(opponentName, opponentType, 'Smarty', 'Smarty', v)
        # preSchoolPoker = PreschoolPoker('Randy', 'Randy', 'Smarty', 'Smarty', v)
        preSchoolPoker.play()
        if preSchoolPoker.winnerPlayerNum() == 2:
            smartyWins = smartyWins + 1
            preSchoolPoker.getPlayer2().learn(preSchoolPoker.getPlayer2().getCurrentState(), 1)
        else:
            otherWins = otherWins + 1
            preSchoolPoker.getPlayer2().learn(preSchoolPoker.getPlayer2().getCurrentState(), 0)
        v = preSchoolPoker.getPlayer2().getV()
        print('v:', v)
    # print(v)
    print('Smarty won', smartyWins, 'times.')
    print('Other won', otherWins, 'times.')
    return v, ('smarty Wins', smartyWins), ('other Wins: ', otherWins)


def main():
    vD = teach(1000, 'DeepPreschooler', 'DeepPreschooler')
    vR = teach(1000, 'Randy', 'Randy')
    vO = teach(1000, 'Oddball', 'Oddball')
    # print(vD)
    # print(vR)
    print('-' * 100)
    smartyWins1 = 0
    deepWins = 0
    for i in range(100):
        preSchoolPoker = PreschoolPoker('DeepPreschooler', 'DeepPreschooler', 'Smarty', 'Smarty', vD[0])
        preSchoolPoker.play()
        if preSchoolPoker.winnerPlayerNum() == 2:
            smartyWins1 += 1
        else:
            deepWins += 1

    smartyWins2 = 0
    randyWins = 0
    for i in range(100):
        preSchoolPoker = PreschoolPoker('Randy', 'Randy', 'Smarty', 'Smarty', vR[0])
        preSchoolPoker.play()
        if preSchoolPoker.winnerPlayerNum() == 2:
            smartyWins2 += 1
        else:
            randyWins += 1

    smartyWins2 = 0
    oddWins = 0
    for i in range(100):
        preSchoolPoker = PreschoolPoker('Oddball', 'Oddball', 'Smarty', 'Smarty', vO[0])
        preSchoolPoker.play()
        if preSchoolPoker.winnerPlayerNum() == 2:
            smartyWins2 += 1
        else:
            oddWins += 1

    print('-' * 100)

    print('Smarty won', smartyWins1, 'times.')
    print('DeepPreschooler won', deepWins, 'times.')
    print()
    print('Smarty won', smartyWins2, 'times.')
    print('Randy won', randyWins, 'times.')
    print()
    print('Smarty won', smartyWins2, 'times.')
    print('Oddball won', oddWins, 'times.')


if __name__ == '__main__':
    main()
