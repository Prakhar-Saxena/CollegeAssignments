#!/usr/bin/env python3

from Card import Card


class Hand:
    def __init__(self, cards):
        if len(cards) > 2:
            print('It\'s not a pair.')
            return
        else:
            self.cards = cards[:]

    def __str__(self):
        return ', '.join(self.cards)

    def getHandValue(self):
        if self.numCards() < 2:
            return 0

        card1V = self.cards[0].getCardValue()
        card2V = self.cards[1].getCardValue()
        if card1V == card2V:
            return card1V * 100
        else:
            return card1V + card2V

    def getCards(self):
        return self.cards

    def getCardValues(self):
        cardValues = []
        for card in self.cards:
            cardValues.append(card.getCardValue())
        return cardValues

    def addCard(self, cardValue):
        if self.numCards() > 2:
            print('Can\'t add the card, already have a pair')
            return False
        else:
            self.cards.append(Card(cardValue))
            return True

    def numCards(self):
        return len(self.cards)

    def isPair(self):
        if self.numCards() < 2:
            return False
        if self.cards[0].value == self.cards[1].value:
            return True
        else:
            return False

    def inHand(self, cardValue):
        for card in self.cards:
            if card.getCardValue == cardValue:
                return True
        return False

    def discard1(self):
        return self.discard(1)

    def discard2(self):
        return self.discard(2)

    def discard3(self):
        return self.discard(3)

    def discard(self, cardValue):
        if self.inHand(cardValue):
            return False
        for card in self.cards:
            if card.getCardValue == cardValue:
                self.cards.remove(card)
                print(str(card), 'discarded from hand.')
                return True

    def swapCards(self, cardOutValue, cardInValue):
        if not self.discard(cardOutValue):
            print('Can\'t swap card, because', str(cardOutValue), 'doesn\'t exist in the hand.')
            return False
        else:
            self.addCard(cardInValue)
            return True
