
# imports
import random
import numpy
import math

# import your own modules
import routeinitialization
import routeevaluation
import routeparent_selection
import routerecombination
import routemutation
import routesurvivor_selection
import matplotlib.pyplot as plt

   
def main(orders,genpercent,verbose = 0):
    random.seed()
    numpy.random.seed()

    factor = int(genpercent / 0.2)

    pop_size =  200
    mating_pool_size = int(pop_size*0.5) # has to be even
    tournament_size = 4
    xover_rate = 0.9
    mut_rate = 0.9
    gen_limit = 50
    mu = int(0.8*pop_size)
    lam = int(0.2*pop_size)

    population = routeinitialization.permutation(pop_size, orders)
    gen = 0 # initialize the generation counter
    fitness=[]
    for i in range (0, pop_size):
        fitness.append(routeevaluation.fitness_fun(population[i],orders))

    iterations_without_improvement = 0
    best_result = None
    current_result = 0.0

    while iterations_without_improvement < 5 and gen < gen_limit:
        parents_index = routeparent_selection.tournament(fitness, mating_pool_size, tournament_size)
        random.shuffle(parents_index)
        offspring =[]
        offspring_fitness = []
        i= 0
        while len(offspring) < mating_pool_size:
        
            if random.random() < xover_rate:            
                off1,off2 = routerecombination.pmx(population[parents_index[i]], population[parents_index[i+1]])
            else:
                off1 = population[parents_index[i]].copy()
                off2 = population[parents_index[i+1]].copy()
                
            if random.random() < mut_rate:
                off1 = routemutation.permutation_swap(off1)
            if random.random() < mut_rate:
                off2 = routemutation.permutation_swap(off2)
        
            offspring.append(off1)
            offspring_fitness.append(routeevaluation.fitness_fun(off1,orders))
            offspring.append(off2)
            offspring_fitness.append(routeevaluation.fitness_fun(off2,orders))
            i = i+2 
        population, fitness = routesurvivor_selection.mu_plus_lambda(population, fitness, offspring, offspring_fitness,mu,lam)
        gen = gen + 1  # update the generation counter
        print("route generation", gen, ": best fitness", min(fitness), "average fitness", sum(fitness)/len(fitness))

        if best_result is None or min(fitness) < best_result:
            best_result =  min(fitness)
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1
    if verbose == 1:
        k = 0
        for i in range (0, pop_size):
            if fitness[i] == min(fitness):
                print("best solution", k, population[i], fitness[i])
                k = k+1
                fig, ax = plt.subplots()
                for i, population[i] in enumerate(population[i]):
                    x, y = zip(*population[i])
                    label = f'Route {i+1}'
                    ax.plot(x, y, label=label)
                ax.set_title('All routes')
                ax.legend()
                plt.show()
    solutions = []
    for i in range (0, pop_size):
        if fitness[i] == min(fitness):
            solutions.append([fitness[i],population[i]])
    return solutions




