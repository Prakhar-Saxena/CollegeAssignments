#!/usr/bin/env python3

import Card
import Deck
import Hand

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return self.name + '\n\t Hand: ' + str(self.hand)

    def discard1(self):
        if self.hand.discard1():
            print(self, 'is discarding a 1')
            return True
        else:
            print(self, 'can\'t discard a 1')

    def discard2(self):
        if self.hand.discard2():
            print(self, 'is discarding a 2')
            return True
        else:
            print(self, 'can\'t discard a 2')

    def discard3(self):
        if self.hand.discard3():
            print(self, 'is discarding a 3')

    def discard(self, cardValue):
        if self.hand.discard(cardValue):
            print(self, 'is discarding a ', cardValue)

'''
    def drawCard(self, deck):
        if len(self.hand.numCards()) >= 2:
            print('Player can\'t draw any more cards')
        else:
            self.hand.addCardToHand(deck.drawCard())
            print('now the Player\'s hand has', self.hand)
'''

    def swapCard(self):
        raise NotImplementedError('swapCard() not implemented')
