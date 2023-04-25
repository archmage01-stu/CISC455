import random


def permutation_swap (individual):
    mutant = individual.copy()
    pos1 = random.randint(0, len(individual)-1)
    pos2 = random.randint(0, len(individual)-1)
    mutant[pos1], mutant[pos2] = individual[pos2], individual[pos1]
    return mutant
