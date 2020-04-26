#!/usr/bin/env python3

import random

from Player import Player


class Human(Player):
    def makeAMove(self, deck):
        # print('Human (', self.name, ') enter your move:')
        legalMoves = ['stand', 'discard1', 'discard2', 'discard3']
        print('Move Options: \n\t 1) stand \n\t 2) discard1 \n\t 3) discard2 \n\t 4) discard3 \n')
        inp = input('Human (' + self.name + '), enter your move:')
        while inp not in legalMoves or (inp != 'stand' and not deck.canDraw()):
            if inp != 'stand' and not deck.canDraw():
                inp = input('Invalid Input. Can\'t draw any more cards from the deck.\nHuman (' + self.name + '), enter a valid move:')
            else:
                inp = input('Invalid Input.\nHuman (' + self.name + '), enter a valid move:')
        if inp == 'discard1':  # I don't have to check for canDraw() because of the while loop condition
            cardInValue = deck.drawCard().getCardValue()
            if self.hand.swapCards(1, cardInValue):
                print('Human (', self.name, ') swapped', 1, 'for', cardInValue)
                return True
        elif inp == 'discard2':  # I don't have to check for canDraw() because of the while loop condition
            cardInValue = deck.drawCard().getCardValue()
            if self.hand.swapCards(2, cardInValue):
                print('Human (', self.name, ') swapped', 2, 'for', cardInValue)
                return True
        elif inp == 'discard3':  # I don't have to check for canDraw() because of the while loop condition
            cardInValue = deck.drawCard().getCardValue()
            if self.hand.swapCards(3, cardInValue):
                print('Human (', self.name, ') swapped', 3, 'for', cardInValue)
                return True
        elif inp == 'stand':
            return True
        else:
            return False
