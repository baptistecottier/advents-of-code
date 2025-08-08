"""
Advent of Code - Year 2023 - Day 3
https://adventofcode.com/2023/day/3
"""

from collections import defaultdict
from itertools import product
from re import finditer


def preprocessing(puzzle_input: str) -> tuple[
        set[tuple[tuple[int, int], int, int]],
        dict[str, list[tuple[int, int]]]]:
    """
    Parses the puzzle input into a set of numbers with their positions and a dictionary of symbol
    positions.
    """
    numbers = set()
    symbols = defaultdict(list)
    for y, line in enumerate(puzzle_input.splitlines()):
        for match in finditer(r'[0-9]+', line):
            numbers.add((match.span(), y, int(match.group())))
        for x, c in enumerate(line):
            if c not in "1234567890.":
                symbols[c].append((x, y))
    return numbers, symbols


def solver(numbers: set[tuple[tuple[int, int], int, int]],
           symbols: dict[str, list[tuple[int, int]]]
           ) -> tuple[int, int]:
    """
    Calculates the sum of part numbers adjacent to symbols and the sum of gear ratios for gears in
    a schematic.
    """
    sum_part_numbers = 0
    sum_gear_ratios = 0
    gears = {}

    for ((start, end), y, n) in numbers:
        for (tx, ty) in product(range(start - 1, end + 1), range(y - 1, y + 2)):
            if (tx, ty) in sum(symbols.values(), []):
                sum_part_numbers += n
                if (tx, ty) in symbols['*']:
                    if (tx, ty) in gears:
                        sum_gear_ratios += gears[(tx, ty)] * n
                    else:
                        gears[(tx, ty)] = n

    return sum_part_numbers, sum_gear_ratios
