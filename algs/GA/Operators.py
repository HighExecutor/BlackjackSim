from game.ActionTables import random_counted_strategy, dealer_states, states, deck_count, actions
import random as rnd
from game.Game import Game
import numpy as np

class Individual:
    def __init__(self, table):
        self.table = table

def ind_generate():
    return Individual(random_counted_strategy())

def pop_generation(pop_size):
    return [ind_generate() for _ in range(pop_size)]

def mutation(ind):
    ps = rnd.choice(states)
    ds = rnd.choice(dealer_states)
    dc = rnd.choice(deck_count)
    ind.table[ps][ds][dc] = rnd.choice(actions)

def crossover(ind1, ind2):
    child = dict()
    for ps in states:
        child[ps] = {ds: dict() for ds in dealer_states}
        for ds in dealer_states:
            child[ps][ds] = {c: dict() for c in deck_count}
            for dc in deck_count:
                random_parent = rnd.random()
                if random_parent > 0.5:
                    child[ps][ds][dc] = ind1.table[ps][ds][dc]
                else:
                    child[ps][ds][dc] = ind2.table[ps][ds][dc]
    return Individual(child)

def tournament_selection(pop, pop_size, tournament_size):
    assert (len(pop) > pop_size + tournament_size)
    result = []
    pop.sort(key = lambda x: x.fitness)
    result.append(pop[-1])
    pop.remove(pop[-1])
    for i in range(pop_size - 1):
        tournament = []
        for t in range(tournament_size):
            cur_ind = rnd.choice(pop)
            while cur_ind in tournament:
                cur_ind = rnd.choice(pop)
            tournament.append(cur_ind)
        tournament.sort(key=lambda x: x.fitness)
        winner = tournament[-1]
        result.append(winner)
        pop.remove(winner)
    return result

def fitness(ind):
    results = []
    repeates = 100
    for _ in range(repeates):
        game = Game(ind.table, 7, 2, 100, 5, 2, 10)
        results.append(game())
    return np.mean(results)