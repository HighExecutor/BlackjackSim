__author__ = 'Mishanya'

# enums
signs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'q': 10, 'k': 10,
          'a': [1, 11]}

class Card:
    def __init__(self, sign, suit):
        self.sign = sign
        self.suit = suit
        self.val = values[sign]

    def isAce(self):
        return self.sign == 'a'
