"""
My collection of fitness evaluation methods

Student number:20146990
Student name:Yifan Zhu
"""

#imports
import math
import routemain

def unpack(individual,orders):
    result = [[] for _ in range(max(individual)+1)]
    for i, elem in enumerate(orders):
        result[individual[i]].append(elem)
    return result

def fitness_fun(individual,orders,genpercent,all_fitness,all_solution): 
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
            solutions = routemain.main(deliveryman,genpercent)
            total_distance = total_distance + solutions[0][0]
            s.append(solutions[0][1])
    all_solution.append([total_distance,s])
    all_fitness[key1]=total_distance


    # student code end
    return total_distance


#fitnesstest = [8,7,6,1,2,5,3,4]
#fitness_8queen(fitnesstest)

#write an function that check list c visited all coord and visited pos[n][0] before pos[n][1]