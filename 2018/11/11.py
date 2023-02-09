from itertools import product

def generator(input): return int(input)

def part_1(input):
    return ','.join([str(item) for item in solver(input, 3, 3)[:2]])


def part_2(input):
    return ','.join([str(item) for item in solver(input, 1, 300)])



def solver(input, min_size, max_size):
    max_score = 0
    grid = [[0 for _ in range(300)] for _ in range(300)]
    for x, y in product(range(1, 301), range(1, 301)):
        xx = 10 + x
        grid[y-1][x-1] = ((y * (xx ** 2) + input * xx ) % 1_000) // 100 - 5
    
    for size in range(min_size, max_size + 1):    
        for x, y in product(range(1, 301 - size), range(1, 301 - size)):
            score = sum([sum(grid[y+yy][x:x+size]) for yy in range(size)])
            if score > max_score: 
                max_score = score
                mx, my, msize = x, y, size
                
    return [mx + 1, my + 1, msize]