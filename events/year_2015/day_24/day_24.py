"""Advent of Code - Year 2015 - Day 24"""

from itertools import combinations
from math      import prod


def preprocessing(puzzle_input: str) -> list[int]:
    """Parse puzzle input into a list of package weights as integers."""
    return [int(package) for package in puzzle_input.splitlines()]


def solver(packages: list[int]):
    """
    Solve the quantum entanglement problem for packages with 3 and 4 compartments.
    
    Args:
        packages (list[int]): List of package weights
    
    Yields:
        int: Quantum entanglement for 3 compartments
        int: Quantum entanglement for 4 compartments
    """
    yield get_quantum_entanglement(packages, 3)
    yield get_quantum_entanglement(packages, 4)


def get_quantum_entanglement(packages: list[int], groups: int) -> int:
    """
    Calculate the quantum entanglement of the first valid package group.
    
    Args:
        packages: List of package weights
        groups: Number of groups to divide packages into
        
    Returns:
        The product of weights in the smallest valid first group
    """
    target = sum(packages) // groups
    size = 1
    while True:
        for package in combinations(packages,size):
            if sum(package) == target:
                return prod(package)
        size += 1
