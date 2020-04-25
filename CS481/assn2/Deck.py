#!/usr/bin/env python3

import random

from Card import Card


class Deck:
    def __init__(self, cards):
        self.cards = cards[:]
        random.shuffle(self.cards)

    def __str__(self):
        return 'Cards in Deck:' + ', '.join(self.cards)

    def drawCard(self):
        if len(self.cards) < 1:
            print('Can\' draw any card')
            return
        else:
            print('Before draw\n\t', str(self))
            card = self.cards.pop()
            print(returnCard)
            print('After draw\n\t', str(self))
            return card
