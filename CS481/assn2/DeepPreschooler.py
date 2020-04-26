#!/usr/bin/env python3

import random

from Player import Player


class DeepPreschooler(Player):
    def makeAMove(self, deck):
        if not self.hand.hasPair() and self.hand.hasA(1) and deck.canDraw():
            cardInValue = deck.drawCard().getCardValue()
            if self.hand.swapCards(1, cardInValue):
                print('DeepPreschooler (', self.name, ') swapped', 1, 'for', cardInValue)
                return True
        return False
