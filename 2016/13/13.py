from AoC_tools import bfs
from itertools import product

def generator(input): 
    n = int(input)
    maze = set()
    for x, y in product(range(50), repeat = 2):
        v = x * (x + 3 + 2 * y) + y * (1 + y) + n 
        if bin(v).count('1') % 2 == 0: 
            maze.add((x, y))
    return maze

def part_1(walls): 
    return bfs(walls, (1,1), (31, 39))

def part_2(walls): 
    distances = (bfs(walls, (1,1) , (x, y), 50) != None for x in range(50) for y in range(50 - x))
    return sum(distances)
