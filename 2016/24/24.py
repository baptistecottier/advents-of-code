from itertools import permutations, pairwise
from aoctools.functions import bfs

def parser(input): 
    grid        = set()
    coordinates = {}
    distances   = {}    
    
    for y, row in enumerate(input.splitlines()):
        for x, c in enumerate(row):
            if c != '#':
                grid.add((x, y))
                if c.isdigit(): coordinates[int(c)] = ((x, y))
                
    for src in range(8):
        for dst in range(src + 1, 8):
            distance = bfs(grid, coordinates[src], coordinates[dst])
            distances[(src, dst)] = distance
            distances[(dst, src)] = distance
    return distances

def solver(distances):
    paths = set()
    for path in permutations(range(1, 8)):
        trip_length = distances[(0, path[0])] + sum(distances[(src, dst)] for src, dst in pairwise(list(path)))
        back_length = distances[(path[-1] , 0)]
        paths.add((trip_length, back_length))
        
    yield min(trip        for trip, _    in paths)
    yield min(trip + back for trip, back in paths)