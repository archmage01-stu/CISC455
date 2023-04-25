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
    # If there are no missing genes, return the offspring sequence;
    # If there are missing genes, traverse the offspring sequence and add the missing genes to the offspring


def permutation_cut_and_crossfill (parent1, parent2):
    pos = random.randint(0, len(parent1) - 1)
    #Cut two parents at the cutting point and cross combine gene sequences according to the cutting point to generate two offspring
    offspring1 = parent1[:pos] + parent2[pos:]
    offspring2 = parent2[:pos] + parent1[pos:]

    offspring1 = repair_permutation(offspring1, parent1)
    # Call repair_ Permutation function to repair possible duplicate or missing genes in offspring
    offspring2 = repair_permutation(offspring2, parent2)

    return offspring1, offspring2