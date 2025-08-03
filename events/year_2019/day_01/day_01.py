"""
Advent of Code - Year 2019 - Day 1
https://adventofcode.com/2019/day/1
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts puzzle input string to a list of integers by splitting on newlines.
    """
    return list(int(item) for item in puzzle_input.splitlines())


def solver(modules: list[int]) -> Iterator[int]:
    """
    Calculates total fuel requirements for modules including additional fuel needed for the fuel
    itself.
    """
    fuel = 0
    modules = compute_fuel(modules)
    fuel += sum(modules)
    yield fuel

    while modules:
        modules = compute_fuel(modules)
        fuel += sum(modules)

    yield fuel


def compute_fuel(modules: list[int]) -> list[int]:
    """
    Calculates fuel requirements for modules by dividing mass by 3 and subtracting 2, filtering out
    modules with mass <= 5.
    """
    return [item // 3 - 2 for item in modules if item > 5]
