"""
Advent of Code - Year 2017 - Day 23
https://adventofcode.com/2017/day/23
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Extract numerical values from every third element of the puzzle input.
    """
    instructions = [
        int(item) for item in puzzle_input.split()[2::3] if not item.isalpha()
    ]
    return instructions


def solver(instructions: list[int]) -> tuple[int, int]:
    """
    Solves a computational problem based on given instructions.

    Args:
        instructions (list): Numerical parameters for the computation

    Yields:
        int: First, the product of two calculated values p and q
        int: Then, the count of non-prime numbers in a specific range
    """
    p = instructions[0] - instructions[7]
    q = instructions[0] - instructions[8]

    h = 0
    b = instructions[0] * instructions[3] - instructions[4]
    c = b - instructions[5]
    step = -instructions[-2]

    for i in range(b, c + 1, step):
        d = instructions[7]
        while i % d != 0:
            d += 1
        if i != d:
            h += 1
    return p * q, h
