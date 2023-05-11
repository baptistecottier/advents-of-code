from itertools import product 
from math import prod

def generator(input):
    return [[9 for _ in range(len(input.splitlines()[0])+2)]] + [[9] + [int(item) for item in line] + [9] for line in input.splitlines()] + [[9 for _ in range(len(input.splitlines()[0])+2)]]

def part_1(input): 
    return len(low_points(input)) + sum(input[y][x] for x, y in low_points(input))

def part_2(input):    
    return prod(sorted(basin_size(input, pos, []) for pos in  low_points(input))[-3:])  

def low_points(heightmap):
    return {(x, y) for x, y in product(range(1, len(heightmap[0]) - 1), range(1, len(heightmap) - 1)) if heightmap[y][x] < min(heightmap[y + ty][x + tx] for tx, ty in [(-1,0),(0,-1),(1,0),(0,1)])}
    
def basin_size(heigtmap, pos, visited):
    x, y = pos
    if heigtmap[y][x] == 9 or (x, y) in visited: return 0
    else: 
        visited.append(pos)
        return 1 + sum(basin_size(heigtmap, (x + dx, y + dy), visited) for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)])