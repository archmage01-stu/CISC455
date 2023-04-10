"""
My collection of recombination methods

Student number:20146990
Student name:Yifan Zhu
"""

#imports
import random

def pmx(parent1, parent2):
    """
    Perform partially mapped crossover (PMX) on two parent solutions.
    """
    # Choose two random points in the chromosome
    point1 = random.randint(0, len(parent1) - 1)
    point2 = random.randint(0, len(parent1) - 1)

    # Make sure point1 is less than point2
    if point1 > point2:
        point1, point2 = point2, point1

    # Initialize the offspring as a copy of parent1
    offspring1 = parent1[:]
    offspring2 = parent2[:]

    # Map the segment between point1 and point2 from parent2 to offspring1
    for i in range(point1, point2 + 1):
        # Find the corresponding element in parent2
        element = parent2[i]

        # If the element is not already in offspring1, find the corresponding element in parent1
        if element not in offspring1[point1:point2 + 1]:
            j = parent1.index(element)

            # Replace the element in parent2 with the corresponding element in parent1
            while offspring1[j] in offspring1[point1:point2 + 1]:
                j = parent1.index(parent2[j])
            offspring1[j] = element

    # Map the segment between point1 and point2 from parent1 to offspring2
    for i in range(point1, point2 + 1):
        # Find the corresponding element in parent1
        element = parent1[i]

        # If the element is not already in offspring2, find the corresponding element in parent2
        if element not in offspring2[point1:point2 + 1]:
            j = parent2.index(element)

            # Replace the element in parent1 with the corresponding element in parent2
            while offspring2[j] in offspring2[point1:point2 + 1]:
                j = parent2.index(parent1[j])
            offspring2[j] = element

    return offspring1, offspring2