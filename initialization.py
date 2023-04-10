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
    for i in range(pop_size):
        all_numbers = list(range(0, workers)) + [random.randint(0, workers-1) for x in range(len(orders)-workers)]
        random.shuffle(all_numbers)
        population.append(all_numbers)
    #student code end
    
    return population                     
