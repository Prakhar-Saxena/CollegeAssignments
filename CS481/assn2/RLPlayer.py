#!/usr/bin/env python3

import random

from Card import Card
from Hand import Hand
from Player import Player


class RLPlayer(Player):
    actions = ['stand', 'discard1', 'discard2', 'discard3']

    def __init__(self, name, deck, v):
        self.name = name
        if deck.canDraw2():
            card1 = deck.drawCard()
            card2 = deck.drawCard()
            self.hand = Hand([card1, card2])
            print(self.name, 'initialised with ', str(self.hand))
            self.v = v
        else:
            print('Can\'t instantiate Player, because can\'t draw 2 cards from teh deck')

    def getCurrentState(self):
        cardValues = self.hand.getCardValues()
        return tuple(sorted((cardValues[0], cardValues[1])))

    def getStatesOnMove(self, move):
        possibleStates = []
        currentState = self.getCurrentState()
        legalMoves = self.getLegalMoves()
        if move not in legalMoves:
            return None
        else:
            for legalMove in legalMoves:
                testHand = Hand([Card(currentState[0]), Card(currentState[1])])
                testHand.s

    def getLegalMoves(self):
        legalMoves = []
        legalMoves.append(0)  # stand
        if self.hand.hasA(1):
            legalMoves.append(1)
        if self.hand.hasA(2):
            legalMoves.append(2)
        if self.hand.hasA(3):
            legalMoves.append(3)
        return legalMoves

    def swapCards(self, cardOutValue, deck):
        legalValues = self.getLegalMoves()
        if deck.canDraw() and cardOutValue in legalValues:
            cardInValue = deck.drawCard().getCardValue()
            if self.hand.swapCards(cardOutValue, cardInValue):
                print('RLPlayer (', self.name, ') swapped', cardOutValue, 'for', cardInValue)
                return True
        return False

    def makeAMove(self, deck):
        currentState = self.getCurrentState()
        legalMoves = self.getLegalMoves()
        maxV = 0
        for i in self.v:

            if i[0] > maxV:
                maxV
        return
