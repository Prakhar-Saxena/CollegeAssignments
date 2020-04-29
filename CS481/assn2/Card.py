#!/usr/bin/env python3

class Card:
    def __init__(self, value):
        self.value = int(value)

    def __str__(self):
        return str(self.value)

    # def __eq__(self, other):
    #     return self.value == other.getCardValue()
    #
    # def __ne__(self, other):
    #     return not self.value < other.getCardValue()
    #
    # def __lt__(self, other):
    #     return self.value < other.getCardValue()
    #
    # def __le__(self, other):
    #     return self.value <= other.getCardValue()
    #
    # def __gt__(self, other):
    #     return self.value > other.getCardValue()
    #
    # def __ge__(self, other):
    #     return self.value >= other.getCardValue()

    def getCardValue(self):
        return int(self.value)
