import math
import routemain

#This function will unpack the orders inorder to pass them separately
def unpack(individual,orders):
    result = [[] for _ in range(max(individual)+1)]
    for i, elem in enumerate(orders):
        result[individual[i]].append(elem)
    return result

#use another gentic algorithm to evaluate fitness
def fitness_fun(individual,orders,all_fitness,all_solution,routehis,routere,routesurvivor): 

    #if the result has been evulated before, we use the result we stored
    key1 = str(individual)
    if key1 in all_fitness:
        return all_fitness[key1]
    total_distance = 0
    result = unpack(individual,orders)
    s = []
    for deliveryman in result:
        if deliveryman == []:
            total_distance = total_distance
        else:
            solutions = routemain.main(deliveryman,routehis,routere,routesurvivor)
            total_distance = total_distance + solutions[0][0]
            s.append(solutions[0][1])
    all_solution.append([total_distance,s])
    all_fitness[key1]=total_distance


    return total_distance

