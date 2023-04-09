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

def permutation_swap (individual,orders):
    """Mutate a permutation"""

    mutant = individual.copy()
    delivery_men = random.sample(range(len(individual)), 1)
    delivery_man1 = individual[delivery_men[0]]
    # student code starts
    pos1 = random.randint(0, len(delivery_man1)-1)
    pos2 = random.randint(0, len(delivery_man1)-1)
    mutant[delivery_men[0]][pos1], mutant[delivery_men[0]][pos2] = individual[delivery_men[0]][pos2], individual[delivery_men[0]][pos1]
    # student code ends
    for o in orders:
        for subroute in mutant:
            if o[0] in subroute:
                if o[1] not in subroute[subroute.index(o[0])+1:]:
                    subroute.append(o[1])
    return mutant
