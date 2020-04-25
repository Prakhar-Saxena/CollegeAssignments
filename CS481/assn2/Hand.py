#!/usr/bin/env python3

import Card

class Hand:
    def __init__(self, cards):
        if len(cards) > 2:
            print('It\'s not a pair.')
            return
        else:
            self.cards = cards[:]

    def getHandValue(self):
        if len(self.cards) < 2:
            return 0

        card1V = self.cards[0].getCardValue()
        card2V = self.cards[1].getCardValue()
        if card1V == card2V:
            return card1V * 100
        else:
            return card1V + card2V

    def addCardToHand(card):
        if len(self.cards) > 2:
            print('Can\'t add the card, already ahve a pair')
            return False
        else:
            self.cards.append(Card)
            return True
