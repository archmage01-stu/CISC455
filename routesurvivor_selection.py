"""
My collection of survivor selection methods

Student number:20146990
Student name:Yifan Zhu
"""

#imports
import random


def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness,mu,lam):
    population = []
    fitness = []
    combined_pop = current_pop + offspring
    combined_fitness = current_fitness + offspring_fitness
    sorted_pop, sorted_fitness = zip(*sorted(zip(combined_pop, combined_fitness), key=lambda x: x[1]))

    sorted_pop = list(sorted_pop)
    sorted_fitness = list(sorted_fitness)
    for i, (item1, item2) in enumerate(zip(sorted_pop, sorted_fitness)):
        if item2 == 9999999999:
            sorted_pop = sorted_pop[:i]
            sorted_fitness = sorted_fitness[:i]
            break

    population = list(sorted_pop[:mu])
    population.extend(sorted_pop[-lam:])

    fitness = list(sorted_fitness[:mu])
    fitness.extend(sorted_fitness[-lam:])
    
    return population, fitness

def sus(current_pop, current_fitness, offspring, offspring_fitness):
    offspring, offspring_fitness = zip(*sorted(zip(offspring, offspring_fitness), key=lambda x: x[1]))
    offspring = list(offspring)
    offspring_fitness = list(offspring_fitness)
    for i, (item1, item2) in enumerate(zip(offspring, offspring_fitness)):
        if item2 == 9999999999:
            offspring = offspring[:i]
            offspring_fitness = offspring_fitness[:i]
            break
    #combine the current population and offspring into a single list
    k = len(current_pop)
    population = current_pop + offspring
    fitness = [1/f for f in current_fitness + offspring_fitness]
    #calculate the total fitness of the population
    total_fitness = sum(fitness)
    #calculate the distance between pointers
    distance = total_fitness / k
    # generate a random starting point
    start = random.uniform(0, distance)
    cumulative_fitness = fitness[0]
    #select the individuals using Stochastic Universal Sampling
    selected_pop = []
    selected_fitness = []
    current_point = start
    i = 0
    while len(selected_pop) < k:
        if cumulative_fitness >= start:
            selected_pop.append(population[i])
            selected_fitness.append(1/fitness[i])
            start += distance
        else:
            i += 1
            cumulative_fitness += fitness[i]
    return selected_pop, selected_fitness



