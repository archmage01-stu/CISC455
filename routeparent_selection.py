"""
My collection of parent selection methods

Student number:20146990
Student name:Yifan Zhu
"""

# imports
import random


def MPS(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""

    selected_to_mate = []

    # student code starts
    max_num = max(fitness)
    weights = [num / max_num for num in fitness]
    cumulative_probs = []
    sum = 0
    for prob in weights:
        sum += prob
        cumulative_probs.append(sum)
    cumulative_p = [e/sum for e in cumulative_probs]

    current = 0
    i=0
    r = random.uniform(0,1/mating_pool_size)
    while current<=mating_pool_size-1:
        while r<=cumulative_p[i]:
            selected_to_mate.append(current)
            r = r + 1/mating_pool_size
            current = current + 1
        i=i+1


    # student code ends
    
    return selected_to_mate


def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""

    selected_to_mate = []

    # student code starts
    current = 1
    while current<= mating_pool_size:
        indexs = random.sample(range(0, len(fitness)), tournament_size)
        members = [fitness[e] for e in indexs]
        winner  = min(members)
        winneri = members.index(winner)
        selected_to_mate.append(indexs[winneri])
        current=current+1

    # student code ends
    
    return selected_to_mate


def random_uniform (population_size, mating_pool_size):
    """Random uniform selection"""

    selected_to_mate = []

    # student code starts
    selected_to_mate = random.sample(range(0,population_size),mating_pool_size)

    # student code ends
    
    return selected_to_mate

