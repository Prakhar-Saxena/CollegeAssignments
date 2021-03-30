#!/usr/bin/env python3

import random

from Player import Player


class Oddball(Player):
    def has1(self):
        return self.hand.hasA(1)

    def has3(self):
        return self.hand.hasA(3)

    def hasOdd(self):
        return self.has1() or self.has3()

    def getLowestOdd(self):
        if self.hasOdd() and self.has1():
            return 1
        elif self.hasOdd() and self.has3():
            return 3
        else:
            return 0

    def doit(self, deck):
        lowestOdd = self.getLowestOdd()
        if lowestOdd != 0 and deck.canDraw():
            cardInValue = deck.drawCard().getCardValue()
            if self.hand.swapCards(lowestOdd, cardInValue):
                print('Oddball (', self.name, ') swapped', lowestOdd, 'for', cardInValue)
                return True
        return False
