"""
Advent of Code - Year 2025 - Day 25 (Test for Timeout)
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
    Solves both parts of the puzzle - intentionally slow for timeout testing.
    """
    print("  🐌 Starting intentionally slow computation for timeout demo...")
    
    # Simulate a slow computation that will trigger timeout
    time.sleep(10)  # Sleep for 10 seconds (longer than our 5s timeout)
    
    part1 = 42
    part2 = 84
    
    return part1, part2