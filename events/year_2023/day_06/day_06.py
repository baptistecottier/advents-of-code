"""
Advent of Code - Year 2023 - Day 6
https://adventofcode.com/2023/day/6
"""

# Standard imports
from math import prod
from re import findall

# Third party imports
from numpy import roots


def preprocessing(puzzle_input: str) -> tuple[list[int], list[int]]:
    """
    Parses the puzzle input to extract lists of times and distances, including their concatenated
    integer forms.
    """
    time, distance = puzzle_input.splitlines()

    time = findall(r'[0-9]+', time)
    time.append(''.join(t for t in time))
    time = list(int(t) for t in time)

    distance = findall(r'[0-9]+', distance)
    distance.append(''.join(d for d in distance))
    distance = list(int(d) for d in distance)

    return time, distance


def solver(time: list[int], distance: list[int]) -> tuple[int, int]:
    """
    Calculates the number of ways to win races given lists of times and distances.
    """
    ways = []
    for t, d in zip(time, distance):
        l, h = sorted((int(n.item()) for n in roots([1, - t, d])))
        ways.append(h - l)

    return prod(ways[:-1]), ways[-1]
