"""
Advent of Code - Year 2023 - Day 11
https://adventofcode.com/2023/day/11
"""


def preprocessing(puzzle_input: str) -> list[tuple[int, int]]:
    """
    Parses the puzzle input and returns a list of (x, y) coordinates for each galaxy represented by
    '#'.
    """
    galaxies = []
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append((x, y))
    return galaxies


def solver(galaxies: list[tuple[int, int]], expansion_factor: int = 1_000_000) -> tuple[int, int]:
    """
    Calculates the total Manhattan distance between galaxy pairs, accounting for expanded empty
    rows and columns.
    """
    [xx, yy] = [set(item) for item in list(zip(*galaxies))]
    total = 0
    to_add = 0

    while galaxies:
        (a, b) = galaxies.pop()
        for (c, d) in galaxies:
            total += abs(c - a) + abs(d - b)
            to_add += sum(v not in xx for v in range(min(a, c), max(a, c) + 1))
            to_add += sum(v not in yy for v in range(min(b, d), max(b, d) + 1))

    return total + to_add, total + (expansion_factor - 1) * to_add
