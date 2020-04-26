#!/usr/bin/env python3

from Card import Card
from Deck import Deck
from Hand import Hand


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return self.name + '\n\t Hand: ' + str(self.hand)

    def addCard(self, deck):
        if deck.canDraw() and self.hand.canAdd() :
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
            print(self, 'is discarding a', cardValue)
            return True
        else:
            print(self, 'can\'t discard a', cardValue)
            return False

    def cardsInHand(self):
        return self.hand.numCards()

    def makeAMove(self, deck):
        raise NotImplementedError('swapCard() not implemented')
