from parse import parse
from itertools import product

def generator(input):
    return [parse("#{:d} @ {:d},{:d}: {:d}x{:d}", line)[:5] for line in input.splitlines()]

def part_1(input): 
    grid = solver(input)
    return sum(grid[y][x] == -1 for x, y in product(range(len(grid)), range(len(grid[0]))))

def part_2(input): 
    grid = solver(input)
    for n, _, _, w, h in input[::-1]:
        if sum(grid[y][x] == n for x, y in product(range(len(grid)), range(len(grid[0])))) == w * h :
            return n

        
def solver(input):
    grid_size = 1_000
    visited = []
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for n, dx, dy, w, h in input:
        for x, y in product(range(w), range(h)):
            if grid[dy + y][dx + x] == 0: grid[dy + y][dx + x] = n
            else : grid[dy + y][dx + x] = - 1
    return grid