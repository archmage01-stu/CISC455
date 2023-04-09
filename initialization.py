"""
My collection of initialization methods for different representations

Student number:20146990
Student name:Yifan Zhu
"""

#imports
import random

def permutation (pop_size, workers, orders):
    """initialize a population of permutation"""

    population = []
    # student code begin
    for i in range(0,pop_size):
        routes = [[]] * workers
        for order in orders:
            workerindex = random.randint(0, workers-1)
            if order[0] in routes[workerindex]:
                routes[workerindex].append(order[1])
            else:
                routes[workerindex].append(order[0])
                routes[workerindex].append(order[1])
        population.append(routes)

    #student code end
    
    return population                     

