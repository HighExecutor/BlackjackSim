__author__ = 'Mishanya'

import random as rnd

# enums
actions = ['h', 's', 'd']
states = ['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
          '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a']
dealer_states = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
deck_count = [-1, 0, 1]

class PlayerDealerTable:
    def __init__(self, action_dict):
        self.actions = action_dict

    def action(self, state):
        return self.actions[state[0]][state[1]]

def basic_strategy():
    table = dict()
    # hard
    for ps in ['17', '18', '19', '20']:
        table[ps] = {ds: 's' for ds in dealer_states}
    for ps in ['13', '14', '15', '16']:
        table[ps] = {ds: 's' for ds in ['2', '3', '4', '5', '6']}
        table[ps].update({ds: 'h' for ds in ['7', '8', '9', '10', '11']})
    for ps in ['12']:
        table[ps] = {ds: 'h' for ds in ['2', '3', '7', '8', '9', '10', '11']}
        table[ps].update({ds: 's' for ds in ['4', '5', '6']})
    for ps in ['11']:
        table[ps] = {ds: 'd' for ds in ['2', '3', '4', '5', '6', '7', '8', '9', '10']}
        table[ps].update({ds: 'h' for ds in ['11']})
    for ps in ['10']:
        table[ps] = {ds: 'd' for ds in ['2', '3', '4', '5', '6', '7', '8', '9']}
        table[ps].update({ds: 'h' for ds in ['10', '11']})
    for ps in ['9']:
        table[ps] = {ds: 'd' for ds in ['3', '4', '5', '6']}
        table[ps].update({ds: 'h' for ds in ['2', '7', '8', '9', '10', '11']})
    for ps in ['4', '5', '6', '7', '8']:
        table[ps] = {ds: 'h' for ds in dealer_states}

    # soft
    for ps in ['8a', '9a']:
        table[ps] = {ds: 's' for ds in dealer_states}
    for ps in ['7a']:
        table[ps] = {ds: 's' for ds in ['2', '7', '8']}
        table[ps].update({ds: 'd' for ds in ['3', '4', '5', '6']})
        table[ps].update({ds: 'h' for ds in ['9', '10', '11']})
    for ps in ['6a']:
        table[ps] = {ds: 'd' for ds in ['3', '4', '5', '6']}
        table[ps].update({ds: 'h' for ds in ['2', '7', '8', '9', '10', '11']})
    for ps in ['4a', '5a']:
        table[ps] = {ds: 'd' for ds in ['4', '5', '6']}
        table[ps].update({ds: 'h' for ds in ['2', '3', '7', '8', '9', '10', '11']})
    for ps in ['2a', '3a']:
        table[ps] = {ds: 'd' for ds in ['5', '6']}
        table[ps].update({ds: 'h' for ds in ['2', '3', '4', '7', '8', '9', '10', '11']})
    for ps in ['1a']:
        table[ps] = {ds: 'h' for ds in dealer_states}
    return table

def random_strategy():
    table = dict()
    for ps in states:
        table[ps] = {ds: rnd.choice(actions) for ds in dealer_states}
    return table

def random_counted_strategy():
    table = dict()
    for ps in states:
        table[ps] = {ds: dict() for ds in dealer_states}
        for ds in dealer_states:
            table[ps][ds] = {c: rnd.choice(actions) for c in deck_count}
    return table

