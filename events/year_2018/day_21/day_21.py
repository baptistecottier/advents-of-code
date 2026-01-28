"""
Advent of Code - Year 2018 - Day 21
https://adventofcode.com/2018/day/21

Fast solution that implements the algorithm directly instead of simulating the VM.
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> int:
    """
    Extracts and returns the initial value from line 8 of the puzzle input.
    """

    lines = puzzle_input.splitlines()
    initial_value = int(lines[8].split()[1])
    return initial_value


def generate_sequence(initial_value: int) -> Iterator[int]:
    """
    Generate the sequence of values that the assembly program produces.
    This is a reverse-engineered version of the VM program.
    """
    r1 = 0

    while True:
        r4 = r1 | 65536
        r1 = initial_value

        while True:
            r5 = r4 & 255
            r1 = (r1 + r5) & 16777215
            r1 = (r1 * 65899) & 16777215

            if r4 < 256:
                break
            r4 //= 256

        yield r1


def solver(initial_value: int) -> Iterator[int]:
    """
    Finds the first and last unique values in a sequence before a cycle is detected.
    """
    seen_values = set()
    previous_value = 0
    first_yield = True

    for value in generate_sequence(initial_value):
        if first_yield:
            yield value
            first_yield = False

        if value in seen_values:
            yield previous_value
            return

        seen_values.add(value)
        previous_value = value
