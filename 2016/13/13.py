from aoctools.functions import bfs
from itertools import product

def parser(data): 
    n = int(data)
    maze = set()
    for x, y in product(range(50), repeat = 2):
        v = x * (x + 3 + 2 * y) + y * (1 + y) + n 
        if bin(v).count('1') % 2 == 0: 
            maze.add((x, y))
    return maze


def solver(maze): 
    yield bfs(maze, (1,1), (31, 39))

    distances = [bfs(maze, (1, 1), (x, y), 50) for x in range(51) for y in range(51 - x)]
    yield sum(distance != -1 for distance in distances)
