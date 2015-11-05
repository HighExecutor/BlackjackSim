__author__ = 'Mishanya'

import random as rnd

from game.Card import Card, signs, suits


class Deck:
    def __init__(self):
        self.cards = [Card(sign, suit) for sign in signs for suit in suits]
        self.count = 0

    def shuffle(self):
        rnd.shuffle(self.cards)

    def deal(self):
        card = self.cards.pop(0)
        if card.sign in ['2', '3', '4', '5', '6']:
            self.count += 1
        if card.sign in ['10', 'j', 'q', 'k', 'a']:
            self.count -= 1
        return card

    def size(self):
        return len(self.cards)

# Several decks
class Shoe(Deck):
    def __init__(self, decks_number):
        super().__init__()
        self.decks = decks_number
        for _ in range(decks_number - 1):
            self.cards.extend([Card(sign, suit) for sign in signs for suit in suits])