#!/usr/bin/env python3

class Card:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def getCardValue(self):
        return self.value
