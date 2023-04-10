"""
My collection of recombination methods

Student number:20146990
Student name:Yifan Zhu
"""

#imports
import random

def repair_permutation(offspring, parent):
    missing = set(parent) - set(offspring)
    if len(missing) == 0:
        return offspring
    else:
        for i in range(len(offspring)):
            if offspring[i] in missing:
                for j in range(len(parent)):
                    if parent[j] not in offspring:
                        offspring[i] = parent[j]
                        break
        return offspring

def permutation_cut_and_crossfill (parent1, parent2):
    pos = random.randint(0, len(parent1) - 1)

    # Perform the crossover
    offspring1 = parent1[:pos] + parent2[pos:]
    offspring2 = parent2[:pos] + parent1[pos:]

    offspring1 = repair_permutation(offspring1, parent1)
    offspring2 = repair_permutation(offspring2, parent2)

    return offspring1, offspring2