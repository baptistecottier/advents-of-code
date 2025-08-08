"""
Advent of Code - Year 2023 - Day 8
https://adventofcode.com/2023/day/8
"""

# Standard imports
from collections.abc import Iterator
from math import lcm

# Third party imports
from parse import parse, Result


def preprocessing(puzzle_input: str) -> tuple[list[str], dict[str, dict[str, str]]]:
    """
    Parses the puzzle input into a list of directions and a mapping of positions to their left and
    right transitions.
    """
    directions, insts = puzzle_input.split('\n\n')
    turns = {'R': {}, 'L': {}}

    for inst in insts.splitlines():
        result = parse("{} = ({}, {})", inst)
        if not isinstance(result, Result):
            raise ValueError("Something is wrong with the input format.")
        pos, left, right = result
        turns['L'][pos] = left
        turns['R'][pos] = right

    return list(directions), turns


def solver(directions: list[str], turns: dict[str, dict[str, str]]) -> Iterator[int]:
    """
    Yields the number of steps required for each specified level using the given directions and
    turns mappings.
    """
    for level in [3, 1]:
        yield cnt_steps(directions, turns, level)


def cnt_steps(directions: list[str], turns: dict[str, dict[str, str]], level: int) -> int:
    """
    Calculates the least common multiple of steps required for all starting positions ending with
    'A' to reach a position ending with 'Z', following the given directions and turns.
    """
    poss = [item for item in turns['L'].keys() if item[-level:] == ('A' * (level))]
    times = set()
    s = len(directions)
    for pos in poss:
        cnt = 0
        i = 0
        while pos[-level:] != 'Z' * (level):
            pos = turns[directions[i]][pos]
            cnt += 1
            i = (i + 1) % s
        times.add(cnt)

    return lcm(*times)
