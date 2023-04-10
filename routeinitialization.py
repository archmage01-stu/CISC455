
import random

def permutation (pop_size, orders):
    """initialize a population of permutation"""

    population = []
    # student code begin
    for i in range(0,pop_size):
        route = []
        for order in orders:
            if order[0] in route:
                route.append(order[1])
            else:
                route.append(order[0])
                route.append(order[1])
        population.append(route)

    #student code end
    
    return population                     

