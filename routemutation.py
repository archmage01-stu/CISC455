"""
My colleciton of mutation methods

Student number:20146990
Student name:Yifan Zhu
"""

# imports
import random

def vaildcheck(individual,orders):
    for o in orders:
        for subroute in individual:
            if o[0] in subroute and o[1] in subroute[subroute.index(o[0])+1:]:
                break
            else:
                return False
    return True

def permutation_swap (individual):
    """Mutate a permutation"""

    mutant = individual.copy()
    # student code starts
    pos1 = random.randint(0, len(individual)-1)
    pos2 = random.randint(0, len(individual)-1)
    mutant[pos1], mutant[pos2] = individual[pos2], individual[pos1]
    # student code ends
    return mutant
