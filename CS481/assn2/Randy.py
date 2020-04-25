#!/usr/bin/env python3

import random

import Player

class Randy(Player):
    def swapCard(self):
        cardValues = self.hand.getCardValues()
        cardOutValue = random.choice(cardValues)

