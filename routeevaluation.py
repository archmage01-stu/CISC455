import math
import random
import numpy

def distance(A,B):
    x1, y1 = A
    x2, y2 = B
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def fitness_fun(individual,orders): 
    for o in orders:
        if o[0] in individual and o[1] in individual[individual.index(o[0])+1:]:
            break
        else:
            return 9999999999

    total_distance = 0

    for i in range(len(individual) - 1):
        total_distance += distance(individual[i], individual[i+1])
    return total_distance

