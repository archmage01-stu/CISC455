"""
My collection of recombination methods

Student number:20146990
Student name:Yifan Zhu
"""

#imports
import random

def permutation_cut_and_crossfill (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""
    
    
    # student code begin
    delivery_men = random.sample(range(len(parent1)), 2)
    delivery_man1 = parent1[delivery_men[0]]
    delivery_man2 = parent2[delivery_men[1]]
    
    # Step 2: Select crossover point
    crossover_point1 = random.randint(1, len(delivery_man1)-1)
    crossover_point2 = random.randint(1, len(delivery_man2)-1)
    
    # Step 3: Swap sublists
    child1 = parent1.copy()
    child2 = parent2.copy()
    child1[delivery_men[0]] = delivery_man1[:crossover_point1] + delivery_man2[crossover_point2:]
    child2[delivery_men[1]] = delivery_man2[:crossover_point2] + delivery_man1[crossover_point1:]
    # student code end
    return child1, child2
