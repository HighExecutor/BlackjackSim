__author__ = 'Mishanya'

from Hand import Hand

class Player:
    def __init__(self, action_table, start_bank):
        self.actions = action_table
        self.bank = start_bank
        self.hand = Hand()

    def state(self):
        ace = self.hand.has_ace()
        score = self.hand.score_without_ace()
        aces_number = self.hand.aces_number()
        if not ace:
            return str(score)
        if aces_number == 2:
            return '1a'
        if ace and score < 10:
            return str(score) + 'a'
        return str(score + 1)


    def hit(self, card):
        self.hand.append(card)

    def act(self, state, dealer_state, shoe_state):
        return self.actions[state][dealer_state][shoe_state]


