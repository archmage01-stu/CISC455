"""
My collection of fitness evaluation methods

Student number:20146990
Student name:Yifan Zhu
"""

#imports
import math

def distance(A,B):
    x1, y1 = A
    x2, y2 = B
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance



def fitness_fun(individual,orders): 
    """Compute fitness of an invidual for the 8-queen puzzle (maximization)"""    
    for o in orders:
        for subroute in individual:
            if o[0] in subroute and o[1] in subroute[subroute.index(o[0])+1:]:
                break
            else:
                return 9999999999



    total_distance = 0

    for route in individual:
        for i in range(len(route) - 1):
            total_distance += distance(route[i], route[i+1])
    


    # student code end
    return total_distance


#fitnesstest = [8,7,6,1,2,5,3,4]
#fitness_8queen(fitnesstest)

#write an function that check list c visited all coord and visited pos[n][0] before pos[n][1]