from itertools import permutations, pairwise

def generator(input) :
    return [int(dist.split(' = ')[1]) for dist in input.splitlines()]

def part_1(input) :
    return solver(input, 0)

def part_2(input) :
    return solver(input, -1)
    
def solver(input, pos) : 
    nb_locations = int((2 * len(input)) ** 0.5) + 1
    distances = []
    for route in permutations(range(nb_locations)):
        distance = 0
        for (a, b) in pairwise(route):
            n = min(a, b)
            x = a + b - 2 * n - 1
            index = (n * (2 * nb_locations - n - 1)) / 2 + x
            distance += input[int(index)]
        distances.append(distance)
    distances.sort()
    return distances[pos]