from itertools import permutations, pairwise
from pythonfw.functions import bfs

def preprocessing(input_): 
    grid        = set()
    coordinates = {}
    distances   = {}    
    
    for y, row in enumerate(input_.splitlines()):
        for x, c in enumerate(row):
            if c != '#':
                grid.add((x, y))
                if c.isdigit(): coordinates[int(c)] = ((x, y))
    n_coord = len(coordinates)
    for src in range(n_coord):
        for dst in range(src + 1, n_coord):
            distance = bfs(grid, coordinates[src], coordinates[dst])
            distances[(src, dst)] = distance
            distances[(dst, src)] = distance
    return distances, n_coord

def solver(distances, n_coord):
    paths = set()
    for path in permutations(range(1, n_coord)):
        trip_length = distances[(0, path[0])] + sum(distances[(src, dst)] for src, dst in pairwise(list(path)))
        back_length = distances[(path[-1] , 0)]
        paths.add((trip_length, back_length))
        
    yield min(trip        for trip, _    in paths)
    yield min(trip + back for trip, back in paths)