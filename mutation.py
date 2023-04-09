"""
My colleciton of mutation methods

Student number:20146990
Student name:Yifan Zhu
"""

# imports
import random

def permutation_swap (individual):
    """Mutate a permutation"""

    mutant = individual.copy()
    delivery_men = random.sample(range(len(individual)), 1)
    delivery_man1 = individual[delivery_men[0]]
    # student code starts
    pos1 = random.randint(0, len(delivery_man1)-1)
    pos2 = random.randint(0, len(delivery_man1)-1)
    mutant[delivery_men[0]][pos1], mutant[delivery_men[0]][pos2] = individual[delivery_men[0]][pos2], individual[delivery_men[0]][pos1]
    # student code ends
    
    return mutant
