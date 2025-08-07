"""
Advent of Code - Year 2021 - Day 3
https://adventofcode.com/2021/day/3
"""


def preprocessing(puzzle_input: str) -> tuple[int, set[int]]:
    """
    Parses a multiline string of binary numbers and returns their bit length and a set of their
    integer representations.
    """
    diagnostic = puzzle_input.splitlines()
    return len(diagnostic[0]),  set(int(item, base=2) for item in diagnostic)


def solver(bit_size: int, report: set[int]) -> tuple[int, int]:
    """
    Computes two diagnostic values from a set of integer bit reports.
    """
    gamma_rate = sum(2 ** k * most_common_bit(report, k) for k in range(bit_size))

    ratings = 1
    for b in (0, 1):
        diag, k = report, bit_size
        while len(diag) > 1:
            bit = most_common_bit(diag, k := k - 1) ^ b
            diag = set(item for item in diag if (item >> k) & 1 == bit)
        ratings *= diag.pop()

    return (2 ** bit_size - 1 - gamma_rate) * gamma_rate, ratings


def most_common_bit(report: set[int], pos: int) -> bool:
    """
    Determines the most common bit at a given position in a list of integers.
    """
    return sum(((r >> pos) & 1) for r in report) >= (len(report) / 2)
