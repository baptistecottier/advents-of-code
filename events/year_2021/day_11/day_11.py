"""
Advent of Code - Year 2021 - Day 11
https://adventofcode.com/2021/day/11
"""

from collections import defaultdict
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> dict[int, set[tuple[int, int]]]:
    """
    Parses the puzzle input into a dictionary mapping each octopus energy level to a set of (x, y)
    coordinate tuples.
    """
    octopus = defaultdict(set)

    for y, row in enumerate(puzzle_input.splitlines()):
        for x, n in enumerate(row):
            octopus[int(n)].add((x, y))

    return octopus


def solver(octopus: dict[int, set[tuple[int, int]]]) -> Iterator[int]:
    """
    Simulates the octopus energy levels and flashing process, yielding the total flashes after 100
    steps and the first step when all octopuses flash simultaneously.
    """
    step = 0
    flashed = 0
    neighbours = ((-1, -1), (0, -1), (1, -1),
                  (-1, 0),           (1, 0),
                  (-1, 1),  (0, 1),  (1, 1))

    while len(octopus[0]) != 100:
        if step == 100:
            yield flashed

        octopus = defaultdict(set, {n + 1: pos for n, pos in octopus.items()})
        while octopus[10]:
            x, y = octopus[10].pop()
            octopus[0].add((x, y))

            for nx, ny in neighbours:
                if (x + nx, y + ny) in octopus[0]:
                    continue
                for energy in range(1, 10):
                    if (x + nx, y + ny) in octopus[energy]:
                        octopus[energy].remove((x + nx, y + ny))
                        octopus[energy + 1].add((x + nx, y + ny))
                        break

        flashed += len(octopus[0])
        step += 1
    yield step
