from itertools import product

def generator(input):
    return [[int(item) for item in line] for line in input.splitlines()]

def part_1(input): 
    return compute_steps(input, 100)

def part_2(input): 
    return compute_steps(input, 1_000)
        
def compute_steps(octopus, rounds): 
    flashed = 0
    for r in range(rounds):
        flashed_pos = set()
        for x, y in product(range(10), repeat=2): octopus[y][x] += 1 
        while any(any(k > 9 for k in line) for line in octopus):
            for x, y in product(range(10), repeat=2):
                if octopus[y][x] > 9:
                    flashed_pos.add((x,y))
                    octopus[y][x] = 0
                    for nx, ny in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
                        if (x+nx, y + ny) not in flashed_pos and 0 <= x+nx < 10 and  0 <= y+ny < 10: 
                            octopus[y + ny][x + nx] += 1
        if len(flashed_pos) == 100: return r + 1
        flashed += len(flashed_pos)
    return flashed