"""
Advent of Code - Year 2020 - Day 14
https://adventofcode.com/2020/day/14
"""

from itertools import combinations
from re import findall


def preprocessing(puzzle_input: str) -> list[tuple[int, list[int], list[list[int]]]]:
    """
    Parses the input string into a list of tuples containing a bitmask as an integer, a list of
    unmasked bit positions, and a list of memory assignments.
    """
    initialization_program = []

    for data in puzzle_input.split('mask = ')[1:]:
        data = data.splitlines()
        not_masked = [i for i in range(36) if data[0][::-1][i] == 'X']
        mask = int(data[0].replace('X', '0'), base=2)
        mem = list(list(map(int, findall(r'[0-9]+', d))) for d in data[1:])
        initialization_program.append((mask, not_masked, mem))

    return initialization_program


def solver(initialization_program: list[tuple[int, list[int], list[list[int]]]]) -> tuple[int, int]:
    """
    Processes a list of initialization instructions to simulate two different memory initialization
    behaviors and returns the sum of all values left in memory for each behavior.
    """
    memory = {1: {}, 2: {}}
    for mask, not_masked, mem in initialization_program:
        for adr, val in mem:
            memory[1][adr] = mask + sum((val >> n & 1) * (2 ** n) for n in not_masked)
            result = mask | adr

            for b in not_masked:
                result &= ~(1 << b)

            for size in range(0, 1 + len(not_masked)):
                for bits in combinations(not_masked, size):
                    memory[2][result + sum((2 ** n) for n in list(bits))] = val

    return sum(memory[1].values()), sum(memory[2].values())
