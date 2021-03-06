#!/usr/bin/env python3

from Card import Card


class Hand:
    def __init__(self, cards):
        if len(cards) > 2:
            print('It\'s not a pair.')
            return
        else:
            self.cards = cards[:]
            self.sortCards()

    def __str__(self):
        cardValues = []
        for card in self.cards:
            cardValues.append(str(card.getCardValue()))
        return 'Cards in Hand: ' + ', '.join(cardValues)

    def sortCards(self):
        if self.numCards() > 1:
            if self.cards[0].getCardValue() > self.cards[1].getCardValue():
                self.cards = [self.cards[1], self.cards[0]]
            elif self.cards[0].getCardValue() > self.cards[1].getCardValue():
                self.cards = [self.cards[0], self.cards[1]]
        # self.cards = sorted(self.cards)

    def getHandValue(self):
        if self.numCards() != 2:
            return 0

        card1V = self.cards[0].getCardValue()
        card2V = self.cards[1].getCardValue()
        if card1V == card2V:
            return card1V * 100
        else:
            return card1V + card2V

    def getCards(self):
        self.sortCards()
        return self.cards

    def getCardValues(self):
        self.sortCards()
        cardValues = []
        for card in self.cards:
            cardValues.append(card.getCardValue())
        return cardValues

    def addCard(self, cardValue):
        if self.canAdd():
            self.cards.append(Card(cardValue))
            self.sortCards()
            return True
        else:
            print('Can\'t add the card, already have a pair')
            return False

    def numCards(self):
        return len(self.cards)

    def hasPair(self):
        if self.numCards() < 2:
            return False
        if self.cards[0].getCardValue() == self.cards[1].getCardValue():
            return True
        else:
            return False

    def hasA(self, cardValue):
        for card in self.cards:
            if card.getCardValue() == cardValue:
                return True
        return False

    def canAdd(self):
        return True if self.numCards() < 2 else False

    def discard(self, cardValue):
        if cardValue == 0:
            return True
        if not self.hasA(cardValue):
            return False
        for card in self.cards:
            if card.getCardValue() == cardValue:
                self.cards.remove(card)
                # print(str(card), 'discarded from hand.')
                self.sortCards()
                return True

    def swapCards(self, cardOutValue, cardInValue):
        if not self.discard(cardOutValue):
            print('Can\'t swap card, because', str(cardOutValue), 'doesn\'t exist in the hand.')
            return False
        else:
            self.addCard(cardInValue)
            self.sortCards()
            return True
