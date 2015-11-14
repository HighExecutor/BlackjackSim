from algs.GA.Operators import *
from copy import deepcopy
from game.ActionTables import basic_strategy

class SimpleGA:
    def __init__(self, pop_size, cxpb, mutpb, gens):
        self.gens = gens
        self.pop_size = pop_size
        self.cxpb = cxpb
        self.mutpb = mutpb
        basic_solutin = Individual(basic_strategy())
        print("Basic result = {0}".format(fitness(basic_solutin)))
        self.pop = pop_generation(pop_size - 1) + [basic_solutin]
        print("Initialuzation has been completed")
        for p in self.pop:
            p.fitness = fitness(p)
        print("Initial fitnesses have been evaluated")


    def __call__(self):
        pop = self.pop
        cxpb = self.cxpb
        mutpb = self.mutpb
        gens = self.gens
        pop_size = self.pop_size

        best = None

        for g in range(gens):
            print("gen {0}".format(g))
            children = []
            for i1 in range(len(pop)):
                for i2 in range(len(pop)):
                    if i1 == i2:
                        continue
                    if (rnd.random() < cxpb):
                        child = crossover(pop[i1], pop[i2])
                        child.fitness = fitness(child)
                        children.append(child)

            for i in range(len(pop)):
                p = pop[i]
                if (rnd.random() < mutpb):
                    mutation(p)
                    p.fitness = fitness(p)

            pop.extend(children)
            for p in pop:
                if best is None or best.fitness < p.fitness:
                    best = deepcopy(p)

            pop = tournament_selection(pop, pop_size, 3)

        return best


if __name__ == '__main__':
    pop_size = 20
    gens = 10
    cxpb = 0.5
    mutpb = 0.1

    ga = SimpleGA(pop_size, cxpb, mutpb, gens)
    res = ga()
    print(res.fitness)
    pass



