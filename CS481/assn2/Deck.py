#!/usr/bin/env python3

import random

from Card import Card


class Deck:
    def __init__(self, cards):
        self.cards = cards[:]
        random.shuffle(self.cards)

    def __str__(self):
        cardValues = []
        for card in self.cards:
            cardValues.append(str(card.getCardValue()))
        return 'Cards in Deck: ' + ', '.join(cardValues)

    def numCards(self):
        return len(self.cards)

    def canDraw(self):
        # print('deck still has cards')
        return True if (self.numCards() >= 1) else False

    def canDraw2(self):
        return True if (self.numCards() >= 2) else False

    def drawCard(self):
        if self.canDraw():
            # print('Before draw\n\t', str(self))
            return self.cards.pop()
            # print(card)
            # print('After draw\n\t', str(self))
            # return card
        else:
            print('Can\' draw any card')
            return None
