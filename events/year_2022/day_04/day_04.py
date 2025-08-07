"""
Advent of Code - Year 2022 - Day 4
https://adventofcode.com/2022/day/4
"""

from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Preprocesses the puzzle input string into a list of lists of integers using extract_chunks.
    """
    return extract_chunks(puzzle_input, 4, neg=False)


def solver(pairs: list[list[int]]) -> tuple[int, int]:
    """
    Counts the number of contained and overlapping interval pairs from a list of integer ranges.
    """
    contained = 0
    overlap = 0

    for (s1, e1, s2, e2) in pairs:
        if (s2 - s1) * (e2 - e1) <= 0:
            contained += 1
        if (e2 - s1) * (s2 - e1) <= 0:
            overlap += 1

    return contained, overlap
