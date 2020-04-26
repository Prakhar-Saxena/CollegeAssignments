#!/usr/bin/env python3

import random

from Card import Card
from Deck import Deck
from Hand import Hand
from Player import Player
from Randy import Randy
from DeepPreschooler import DeepPreschooler
from Human import Human

class PreschoolPoker:
    def __init__(self, player1Name, player1Type, player2Name, player2Type):
        initialCardsInDeck = [Card(1), Card(2), Card(3), Card(1), Card(2), Card(3)]
        self.deck = Deck(initialCardsInDeck)
        self.player1 = self.getPlayer(player1Name, player1Type, self.deck)
        self.player2 = self.getPlayer(player2Name, player2Type, self.deck)

    def getPlayer(self, playerName, playerType, deck):
        if playerType == 'Randy':
            return Randy(playerName, deck)
        elif playerType == 'DeepPreschooler':
            return DeepPreschooler(playerName, deck)
        elif playerType == 'Human':
            return Human(playerName, deck)
        else:
            return Player(playerName, deck)

    def winner(self):
        if self.player1.getHandValue() > self.player2.getHandValue():
            return self.player1
        elif self.player1.getHandValue() > self.player2.getHandValue():
            return self.player2
        else:
            return None

    def play(self):
        self.player1.makeAMove(self.deck)
        self.player2.makeAMove(self.deck)
        print('Winner is: ', self.winner())


def main():
    initialCardsInDeck = [Card(1), Card(2), Card(3), Card(1), Card(2), Card(3)]
    deck = Deck(initialCardsInDeck)
    print(deck)
    # player = Player('eh', deck)
    randy = Randy('Random Player', deck)
    # deepPreschooler = DeepPreschooler(deck)
    # Human = Human(deck)
    randy.makeAMove(deck)
    print(deck)


if __name__ == '__main__':
    main()
