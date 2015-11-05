__author__ = 'Mishanya'

class Hand(list):
    def __init__(self):
        super().__init__()

    def has_ace(self):
        for card in self:
            if card.isAce():
                return True
        return False

    def score_without_ace(self):
        n_aced_cards = [card.val for card in self if not card.isAce()]
        return sum(n_aced_cards)

    def score(self):
        ace = self.has_ace()
        sc = self.score_without_ace()
        if ace:
            for _ in range(self.aces_number() - 1):
                sc += 1
            if sc <= 10:
                sc += 11
            if sc > 10:
                sc += 1
        return sc

    def aces_number(self):
        counter = 0
        for card in self:
            if card.isAce():
                counter += 1
        return counter

    def print(self):
        res = ''
        for card in self:
            res += card.sign + ' '
        print(res)

