"""
Advent of Code - Year 2018 - Day 3
https://adventofcode.com/2018/day/3
"""

# Standard imports
from collections import defaultdict
from itertools import product

# First-party imports
from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Extracts claims from puzzle input by splitting into chunks of 5.

    Examples:
        >>> preprocessing("#1 @ 1,3: 4x4\\n#2 @ 3,1: 4x4\\n#3 @ 5,5: 2x2")
        [[1, 1, 3, 4, 4], [2, 3, 1, 4, 4], [3, 5, 5, 2, 2]]
    """
    claims = extract_chunks(puzzle_input, 5)
    return claims


def solver(claims: list[list[int]]) -> tuple[int, int]:
    """
    Solves fabric claim overlap problem by finding overlapping square inches and non-overlapping
    claim ID.

    Args:
        claims: List of claims, each containing [id, x, y, width, height]

    Returns:
        Tuple of (overlapping_square_inches_count, non_overlapping_claim_id)

    Examples:
        >>> solver([[1, 1, 3, 4, 4], [2, 3, 1, 4, 4], [3, 5, 5, 2, 2]])
        (4, 3)
        >>> solver([[1, 0, 0, 2, 2], [2, 1, 1, 2, 2]])
        (1, -1)
    """
    non_overlapping_claim_id = -1
    visited = defaultdict(int)
    for ida, xa, ya, dxa, dya in claims:
        for pos in product(range(xa, xa + dxa), range(ya, ya + dya)):
            visited[pos] += 1

    for ida, xa, ya, dxa, dya in claims:
        if all(visited[pos] == 1
               for pos in product(range(xa, xa + dxa), range(ya, ya + dya))):
            non_overlapping_claim_id = ida

    return sum(n > 1 for n in visited.values()), non_overlapping_claim_id
