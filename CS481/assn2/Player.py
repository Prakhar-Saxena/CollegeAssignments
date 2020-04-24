import Card
import Deck

class Player:
    def __init__(self):
        self.cards = []

    def drawCard(self, deck):
        if len(self.cards) >= 2:
            print('Player can\'t draw any more cards')
        else:
            self.cards.append(deck.drawCard())
        print(cards)
