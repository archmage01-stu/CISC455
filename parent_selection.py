import random


def tournament(fitness, mating_pool_size, tournament_size):
    
    selected_to_mate = []

    current = 1
    while current<= mating_pool_size:
        indexs = random.sample(range(0, len(fitness)), tournament_size)
        members = [fitness[e] for e in indexs]
        winner  = min(members)
        winneri = members.index(winner)
        selected_to_mate.append(indexs[winneri])
        current=current+1

    
    return selected_to_mate

