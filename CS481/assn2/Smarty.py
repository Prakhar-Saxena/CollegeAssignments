#!/usr/bin/env python3

import random

from Card import Card
from Hand import Hand
from Player import Player


class Smarty(Player):
    actions = ['stand', 'discard1', 'discard2', 'discard3']

    def __init__(self, name, deck, alpha):
        self.name = name
        if deck.canDraw2():
            card1 = deck.drawCard()
            card2 = deck.drawCard()
            self.hand = Hand([card1, card2])
            print(self.name, 'initialised with ', str(self.hand))
            self.v = {(1, 1): 0.5,
                      (1, 2): 0.5,
                      (1, 3): 0.5,
                      (2, 2): 0.5,
                      (2, 3): 0.5,
                      (3, 3): 0.5,
                      }
            self.alpha = alpha
        else:
            print('Can\'t instantiate Player, because can\'t draw 2 cards from teh deck')

    def getCurrentState(self):
        return tuple(sorted(self.hand.getCardValues()))

    def getStatesOnMove(self, move):  # 0 means stand; 1 means discard 1; 2 means discard 2; 3 means discard 3
        if move == 0:
            return [self.getCurrentState()]
        if move not in self.getLegalMoves():
            return None
        else:
            possibleStates = []
            currentState = self.getCurrentState()
            for i in range(1, 4):
                testHand = Hand([Card(currentState[0]), Card(currentState[1])])
                testHand.swapCards(move, i)  # don't have to worry about move card existing because it's checked earlier
                possibleStates.append(tuple(sorted(testHand.getCardValues())))
            return possibleStates

    def getProbability(self, stateI, stateJ):  # it's an approximation
        stateI = tuple(sorted(stateI))
        stateJ = tuple(sorted(stateJ))
        if stateI ==  stateJ:  # if both the states are same
            return 1
        intersectionSet = set(stateI).intersection(set(stateJ))
        if len(intersectionSet) == 0:  # if both states have different different cards e.g. (1,2) to (3,3)
            return 0
        deck = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        deck.remove(stateI[0])
        deck.remove(stateI[1])
        changeCard = tuple(set(stateJ).difference(set(stateI)))[0]
        return deck.count(changeCard) / len(deck)



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
        if deck.canDraw() and cardOutValue in self.getLegalMoves():
            cardInValue = deck.drawCard().getCardValue()
            if self.hand.swapCards(cardOutValue, cardInValue):
                print('RLPlayer (', self.name, ') swapped', cardOutValue, 'for', cardInValue)
                return True
        return False

    def getPossibleStates(self):
        possibleStates = []
        for legalMove in self.getLegalMoves():
            possibleStates = possibleStates + self.getStatesOnMove(legalMove)
        return possibleStates


    def doit(self, deck):
        currentState = self.getCurrentState()
        legalMoves = self.getLegalMoves()
        maxV = 0
        moveToStates = {}
        stateProbability = {}
        for legalMove in legalMoves:
            moveToStates[legalMove] = self.getStatesOnMove(legalMove)
        for m in legalMoves:
            statesOnMove = self.getStatesOnMove(m)
            for state in statesOnMove:
                stateProbability[state] = self.getProbability(self.getCurrentState(), state)
        for i in self.v:

            if i[0] > maxV:
                maxV
        return
