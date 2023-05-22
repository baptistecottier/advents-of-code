from itertools import permutations, pairwise

def generator(input):
    return [int(dist.split(' = ')[1]) for dist in input.splitlines()]

def part_1(routes):
    return min(get_distances(routes))

def part_2(routes):
    return max(get_distances(routes))
    
def get_distances(routes): 
    nb_locations = 1 + round((2 * len(routes)) ** 0.5)
    distances = set()
    for route in permutations(range(nb_locations)):
        distance = 0
        for (a, b) in pairwise(route):
            n = min(a, b)
            delta = (a - n) + (b - n) - 1
            index = (n * (2 * nb_locations - n - 1)) // 2 + delta
            distance += routes[index]
        distances.add(distance)
    return distances