"""Advent of Code - Year 2015 - Day 24"""

from itertools import combinations
from math import prod
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a multiline string of integers into a list of integers.

    Args:
        puzzle_input (str): Multiline string where each line is an integer.

    Returns:
        list[int]: List of integers parsed from the input.

    Example:
        >>> preprocessing("1\n2\n3")
        [1, 2, 3]
    """
    return list(map(int, puzzle_input.splitlines()))


def solver(packages: list[int]) -> Iterator[int]:
    """
    Yields the quantum entanglement for dividing packages into 3 and 4 compartments.

    Args:
        packages (list[int]): List of package weights.

    Yields:
        int: Quantum entanglement for each compartment count (3 and 4).

    Example:
        >>> list(solver([1, 2, 3, 4, 5, 7, 8, 9, 10, 11]))
        [99, 44]
    """
    for nb_compartments in [3, 4]:
        yield get_quantum_entanglement(packages, nb_compartments)


def get_quantum_entanglement(packages: list[int], groups: int) -> int:
    """
    Finds the minimal quantum entanglement for dividing packages into groups of equal weight.

    Quantum entanglement is defined as the product of the weights in the first group of minimal
    size.

    Args:
        packages (list[int]): List of package weights.
        groups (int): Number of groups to divide the packages into.

    Returns:
        int: The minimal quantum entanglement for the first group.

    Example:
        >>> get_quantum_entanglement([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 3)
        99
    """
    target = sum(packages) // groups
    size = 1
    while True:
        for package in combinations(packages, size):
            if sum(package) == target:
                return prod(package)
        size += 1
