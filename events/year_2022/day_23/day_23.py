"""
Advent of Code - Year 2022 - Day 23
https://adventofcode.com/2022/day/23
"""

from collections import Counter


def preprocessing(puzzle_input: str) -> list[tuple[int, int]]:
    """
    Parses the puzzle input and returns a list of (x, y) tuples representing the positions of elves
    marked by '#' characters.
    """
    elves = []
    x = y = -1
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                elves.append((x, y))
    return elves


def solver(elves: list[tuple[int, int]]):
    """
    Simulates elf movement according to specified rules and yields the result after 10 rounds and
    the round when no elf moves.
    """
    neighbours = {(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)}
    checks = [{(-1, -1), (0, -1), (1, -1)}, {(-1, 1), (0, 1), (1, 1)},
              {(-1, -1), (-1, 0), (-1, 1)}, {(1, -1), (1, 0), (1, 1)}]
    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    i = -1
    while True:
        i += 1
        new_elves = []
        for (x, y) in elves:
            if all((x + dx, y + dy) not in elves for (dx, dy) in neighbours):
                new_elves.append((x, y))
                continue
            if all((x + dx, y + dy) not in elves for (dx, dy) in checks[i % 4]):
                dx, dy = direction[i % 4]
            elif all((x + dx, y + dy) not in elves for (dx, dy) in checks[(i + 1) % 4]):
                dx, dy = direction[(i + 1) % 4]
            elif all((x + dx, y + dy) not in elves for (dx, dy) in checks[(i + 2) % 4]):
                dx, dy = direction[(i + 2) % 4]
            elif all((x + dx, y + dy) not in elves for (dx, dy) in checks[(i + 3) % 4]):
                dx, dy = direction[(i + 3) % 4]
            else:
                new_elves.append((x, y))
                continue

            new_elves.append((x + dx, y + dy))
        relves = []

        cnts = Counter(new_elves)
        for k, new_elf in enumerate(new_elves):
            if cnts[new_elf] > 1:
                relves.append(elves[k])
            else:
                relves.append(new_elf)

        if set(elves) == set(relves):
            yield i + 1
            break
