"""
Advent of Code - Year 2017 - Day 24
https://adventofcode.com/2017/day/24
"""

from copy import deepcopy
from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Extract and convert chunks of input data into a list of 2-element lists of integers.
    """
    return extract_chunks(puzzle_input, 2)


def solver(connections: list[list[int]]) -> tuple[int, int]:
    """
    Solve bridge building puzzle by finding the strongest and longest bridges.

    Args:
        connections: List of port connections, each represented as a list of two integers.

    Yields:
        int: First, the strength of the strongest bridge.
        int: Second, the strength of the longest (and if tied, strongest) bridge.
    """
    bridges = build_bridges(connections, 0, [(0, 0)])
    return max(bridges, key=lambda x: x[1])[1], max(bridges)[1]


def build_bridges(
    components: list[list[int]], port: int, strength: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """
    Build bridges recursively from components with matching ports.

    Args:
        components: List of component pairs [port1, port2]
        port: Current port value to match
        strength: List of tuples (length, total_strength) for built bridges

    Returns:
        List of tuples representing all possible bridge configurations

    Example:
        >>> components = [[0, 2], [2, 2], [2, 3]]
        >>> build_bridges(components, 0, [(0, 0)])
        [(2, 7), (1, 2)]
    """

    candidates = [c for c in components if port in c]
    if not candidates:
        return strength

    for c in candidates:
        cc = deepcopy(components)
        cc.remove(c)
        strength += build_bridges(
            cc, sum(c) - port, [(strength[0][0] + 1, strength[0][1] + sum(c))]
        )

    return strength
