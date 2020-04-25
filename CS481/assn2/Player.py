#!/usr/bin/env python3

import Card
import Deck
import Hand

class Player:
    def __init__(self):
        self.Hand = Hand([])

    def drawCard(self, deck):
        if len(self.cards) >= 2:
            print('Player can\'t draw any more cards')
        else:
            self.cards.append(deck.drawCard())
        print(cards)
