import random

def permutation (pop_size, workers, orders):
   #initialize a population

    population = []
    for i in range(pop_size):
        all_numbers = list(range(0, workers)) + [random.randint(0, workers-1) for x in range(len(orders)-workers)]
        random.shuffle(all_numbers)
        population.append(all_numbers)
    
    return population                     
