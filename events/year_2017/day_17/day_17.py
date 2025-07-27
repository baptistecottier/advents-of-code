"""
Advent of Code - Year 2017 - Day 17
https://adventofcode.com/2017/day/17
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> int:
    """
    Converts the puzzle input string to an integer.
    """
    return int(puzzle_input)


def solver(n_steps: int) -> Iterator[int]:
    """
    Simulates a circular buffer spinlock and computes values at specified positions.

    The function iterates through a simulation of 50 million steps, where each step involves
    calculating a new position and inserting a value. It tracks:
    - The value at position 1 after 50 million insertions
    - The value immediately after 2017 in the state list after 2017 insertions

    Args:
        n_steps (int): Number of steps to move forward in each iteration

    Yields:
        int: First, the value that comes after 2017 in the buffer after 2017 insertions
        int: Second, the value at position 1 after 50 million insertions
    """
    value = 0
    pos = 0
    state = [0]
    for i in range(50_000_000):
        pos = 1 + (pos + n_steps) % (i + 1)
        if pos == 1:
            value = i + 1
        if i < 2017:
            state.insert(pos, i + 1)
        if i == 2017:
            yield state[state.index(2017) + 1]
    yield value
