#!/usr/bin/env python3

class Card:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.getCardValue() == other.getCardValue()

    def __ne__(self, other):
        return not self.getCardValue() < other.getCardValue()

    def __lt__(self, other):
        return self.getCardValue() < other.getCardValue()

    def __le__(self, other):
        return self.getCardValue() <= other.getCardValue()

    def __gt__(self, other):
        return self.getCardValue() > other.getCardValue()

    def __ge__(self, other):
        return self.getCardValue() >= other.getCardValue()

    def getCardValue(self):
        return self.value
