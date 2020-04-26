#!/usr/bin/env python3

import random

from Player import Player


class Randy(Player):
    def makeAMove(self, deck):
        cardValues = self.hand.getCardValues()
        cardOutValue = random.choice(cardValues)
        if deck.canDraw() and self.cardsInHand() == 2:
            cardIn = deck.drawCard().getCardValue()
            if self.hand.swapCards(cardOutValue, cardIn):
                print('Randy (', self.name, ') swapped', cardOutValue, 'for', cardIn)
                return True
        return False
