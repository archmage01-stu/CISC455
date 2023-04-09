"""
My collection of survivor selection methods

Student number:20146990
Student name:Yifan Zhu
"""

#imports
import random


def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu+lambda selection"""
    population = []
    fitness = []

    # student code starts
    allp = current_pop+offspring
    allf = current_fitness+offspring_fitness
    selectedzip = sorted(zip(allf, allp), reverse=False)[:len(allp)]
    selected = [list(t) for t in zip(*selectedzip)]
    fitness = selected[0]
    population = selected[1]
    # student code ends
    
    return population, fitness


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    population = []
    fitness = []

    # student code starts
    current_pop = [x for _, x in sorted(zip(current_fitness, current_pop), key=lambda pair: pair[0], reverse=True)]
    current_fitness = sorted(current_fitness, reverse=True)
    offspring = [x for _, x in sorted(zip(offspring_fitness, offspring), key=lambda pair: pair[0], reverse=True)]
    offspring_fitness = sorted(offspring_fitness, reverse=True)
    index = 0
    for i in range(0,len(current_pop)):
        if current_fitness[i]<offspring_fitness[index]:
            population.append(offspring[index])
            fitness.append(offspring_fitness[index])
            index = index + 1
            if index == len(offspring):
                break
        population.append(current_pop[i])
        fitness.append(current_fitness[i])
    # student code ends
    
    return population, fitness


def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """random uniform selection"""
    population = []
    fitness = []

    # student code starts
    allp = current_pop+offspring
    allf = current_fitness+offspring_fitness

    indexs = random.sample(range(0, len(allp)), len(current_pop))
    population=[allp[e] for e in indexs]
    fitness=[allf[e] for e in indexs]
    # student code ends
    
    return population, fitness


