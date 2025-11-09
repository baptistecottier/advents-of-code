"""
Advent of Code - Year 2025 - Day 99 (Test Day for Timeout)
Test day to demonstrate timeout functionality
"""

import time


def preprocessing(puzzle_input: str) -> str:
    """
    Processes the puzzle input into a suitable data structure.
    """
    return puzzle_input.strip()


def solver(data: str) -> tuple[int, int]:
    """
    Solves both parts of the puzzle.
    Returns a tuple (part1_result, part2_result).
    
    This solver intentionally takes a long time for testing timeout.
    """
    print("  Starting long computation...")
    
    # Simulate a very slow computation for part 1
    time.sleep(120)  # Sleep for 2 minutes
    part1 = 42
    
    # Simulate another slow computation for part 2
    time.sleep(60)   # Sleep for 1 more minute
    part2 = 84
    
    return part1, part2