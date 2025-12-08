"""
Advent of Code - Year 2025 - Day 7
https://adventofcode.com/2025/day/7
"""

from collections import defaultdict


def preprocessing(puzzle_input: str) -> tuple[set[tuple[int, int]], int, int]:
    """
    Parse puzzle input to extract splitter positions and starting coordinates.
    """
    start = None
    splitters = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == '^':
                splitters.add((x, y))
            if c == 'S':
                start = (x, y)
    if start is None:
        raise ValueError("No start found!")
    return (splitters, *start)


def solver(splitters, beam, y_start) -> tuple[int, int]:
    """
    Simulates beam splitting through splitters and returns the number of splits and final beam
    count.
    """
    beams = {beam: 1}
    n_splits = 0

    for y in range(
            y_start,
            max(y for _, y in splitters) + 1,
            2):
        new_beams = defaultdict(int)

        for x, n_beams in beams.items():
            if (x, y) in splitters:
                new_beams[x - 1] += n_beams
                new_beams[x + 1] += n_beams
                n_splits += 1
            else:
                new_beams[x] += beams[x]
        beams = new_beams

    return n_splits, sum(beams.values())
