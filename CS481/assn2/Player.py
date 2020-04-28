#!/usr/bin/env python3

from Card import Card
from Deck import Deck
from Hand import Hand


class Player:
    def __init__(self, name, deck):
        self.name = name
        if deck.canDraw2():
            card1 = deck.drawCard()
            card2 = deck.drawCard()
            self.hand = Hand([card1, card2])
            print(self.name, 'initialised with ', str(self.hand))
        else:
            print('Can\'t instantiate Player, because can\'t draw 2 cards from teh deck')

    def __str__(self):
        return self.name + '\n\t ' + str(self.hand)

    def getHandValue(self):
        return self.hand.getHandValue()

    def addCard(self, deck):
        if deck.canDraw() and self.hand.canAdd():
            deck.drawCard()
            return True
        else:
            return False

    def discard1(self):
        return self.discard(1)

    def discard2(self):
        return self.discard(2)

    def discard3(self):
        return self.discard(3)

    def discard(self, cardValue):
        if self.hand.discard(cardValue):
            # print(self, 'is discarding a', cardValue)
            return True
        else:
            # print(self, 'can\'t discard a', cardValue)
            return False

    def cardsInHand(self):
        return self.hand.numCards()

    def doit(self, deck):
        raise NotImplementedError('makeAMove() not implemented')
