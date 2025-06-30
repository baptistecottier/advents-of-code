"""Advent of Code - Year 2015 - Day 17"""

from itertools import combinations


def preprocessing(puzzle_input: str) -> tuple[int, ...]:
    """Process input into tuple of container sizes.

    Args:
        puzzle_input (str): Raw puzzle input string with container sizes.

    Returns:
        tuple[int]: Container sizes as integers.
    """
    return tuple(int(container) for container in puzzle_input.splitlines())


def solver(*containers: tuple[int], liters: int = 150):
    """
    Calculates container combinations that can hold a specified amount of liquid.

    This function iterates through all possible combinations of containers to find those
    that can exactly hold the specified number of liters. It yields two results:
    1. The total number of valid combinations (all sizes)
    2. The number of combinations using the minimum number of containers

    Args:
        *containers (tuple[int]): A variable number of integer arguments representing container
                                  sizes
        liters (int, optional): The target volume to fill. Defaults to 150.

    Yields:
        tuple[int, int]: First yield is (2, count) where count is the number of combinations using
                         minimum containers.
                         Second yield is (1, count) where count is the total number of valid
                         combinations.
    """
    total = 0
    found = False
    for size in range(len(containers)):
        size_total = 0
        for comb in combinations(containers, size):
            if sum(comb, start = 0) == liters:
                size_total += 1
        if not found and size_total != 0:
            found = True
            yield (2, size_total)
        total += size_total
    yield (1, total)
