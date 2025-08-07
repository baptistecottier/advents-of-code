"""
Advent of Code - Year 2022 - Day 5
https://adventofcode.com/2022/day/5
"""

# Standard imports
from collections.abc import Iterator

# First party imports
from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> tuple[list[str], list[list[int]]]:
    """
    Parses the puzzle input into a list of cargo stacks and a list of move instructions.
    """
    cargo, moves = puzzle_input.split('\n\n')
    moves = extract_chunks(moves, 3)
    floors = cargo.splitlines()[::-1]
    width = len(floors[0].replace(' ', ''))
    cargo = ["" for _ in range(width)]

    for floor in floors[1:]:
        crates = floor.split('[')
        pos = len(crates[0]) // 4
        for crate in crates[1:]:
            cargo[pos] += crate[0]
            pos += 1 + (crate.count(' ') // 4)

    return cargo, moves


def solver(cargos_init: list[str], moves: list[list[int]]) -> Iterator[str]:
    """
    Simulates cargo moves according to given instructions and yields the top item of each stack for
    two versions of the move operation.
    """
    cargos = {-1: (cargos_init), 1: list(cargos_init)}
    for qty, src, dst in moves:
        for version, cargo in cargos.items():
            cargo[dst - 1] += cargo[src - 1][-qty:][::version]
            cargo[src - 1] = cargo[src - 1][:-qty]

    for cargo in cargos.values():
        yield ''.join([stack[-1] for stack in cargo])
