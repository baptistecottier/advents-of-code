from collections    import defaultdict
from itertools      import combinations

"""
Browse puzzle input and retrieve positions of the antennas. As we won't need
antennas name to solve the puzzles, only the posiions grouped by antenna are
returned.
"""
def preprocessing(puzzle_input): 
    antennas = defaultdict(list)
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c != '.': antennas[c].append((x, y))
    return antennas.values(), x, y
            

"""
For each antenna and for each pair of locations by antenna, we register all
positions in line with these pair of locations. In order to solve part one, we
diffentiate locations directly next to the antenna from the other ones.
"""
def solver(antennas, width, height):
    locations = {0: set(), 1: set()}
    for antenna in antennas:
            for ((xa, ya), (xb, yb)) in combinations(antenna, 2):
                (dx, dy) = (xb - xa, yb - ya)
                for delta in range(max(xa, ya)):
                    for x, y in ((xa - delta * dx, ya - delta * dy), (xb + delta * dx, yb + delta * dy)):
                        if (0 <= x <= width) and (0 <= y <= height):
                            locations[delta == 1].add((x, y))

    yield len(locations[1])
    yield len(locations[0].union(locations[1]))
