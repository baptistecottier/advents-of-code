from itertools import product

def preprocessing(puzzle_input):
    galaxies = list()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == '#' : galaxies.append((x, y))
    return galaxies

def solver(galaxies, expansion_factor = 1_000_000):
    [xx, yy] = [set(item) for item in list(zip(*galaxies))]
    total = 0
    to_add = 0

    while galaxies:
        (a, b) = galaxies.pop()
        for (c, d) in galaxies:
            total += abs(c - a) + abs(d - b)
            to_add += sum(v not in xx for v in range(min(a, c), max(a, c) + 1))
            to_add += sum(v not in yy for v in range(min(b, d), max(b, d) + 1))
        
    yield total + to_add
    yield total + (expansion_factor - 1) * to_add



