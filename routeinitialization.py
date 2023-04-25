import random

def permutation (pop_size, orders):
    

    population = []
    for i in range(0,pop_size):
        route = []
        for order in orders:
            if order[0] in route:
                route.append(order[1])
                # If the first position of the order is already in the path, add the second position of the order to the path
            else:
                route.append(order[0])
                route.append(order[1])
                # or add both of them
        population.append(route)

    
    return population                     

