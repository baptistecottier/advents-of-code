"""
Test case for partial solutions - one part correct, one part wrong
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> str:
    """Simply return the input as is."""
    return puzzle_input.strip()


def solver(puzzle_input: str) -> Iterator[int]:
    """
    Test solver that returns two different answers to simulate partial solution.
    """
    _ = puzzle_input  # Use the input parameter to avoid lint warnings
    
    # Part 1: This should be "correct" (we'll mock this)
    part1 = 42
    
    # Part 2: This should be "wrong" (we'll mock this)
    part2 = 999
    
    yield part1
    yield part2