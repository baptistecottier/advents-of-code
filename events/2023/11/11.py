from itertools import product

def preprocessing(input):
    galaxies = list()
    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line):
            if c == '#' : galaxies.append((x, y))
    return galaxies

def solver(galaxies):
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
    yield total + 999_999 * to_add



