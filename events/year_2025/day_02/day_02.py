"""
Advent of Code - Year 2025 - Day 2
https://adventofcode.com/2025/day/2
"""

from collections import defaultdict


def preprocessing(puzzle_input: str) -> list[tuple[int, int]]:
    """
    Parses a comma-separated string of integer ranges into a list of tuples.
    """
    ranges = puzzle_input.split(',')
    lst_ranges = []
    for rng in ranges:
        lst_ranges.append(tuple(map(int, rng.split('-'))))
    return lst_ranges


def solver(ranges: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Calculates the sum of product IDs with repeated digit patterns in given ranges and returns the
    sum for pattern repeted twice and the total sum for all patterns appearing.
    """
    invalid_register = defaultdict(int)

    for start, end in ranges:
        for product_id in range(max(11, start), end + 1):
            str_id = str(product_id)
            half_length = len(str_id) // 2

            # We need to start by 2 to ensure cases as '9999'
            # won't be counted for length 1
            if str_id[:half_length] * 2 == str_id:
                invalid_register[2] += product_id
                continue

            if str_id[0] * len(str_id) == str_id:
                invalid_register[1] += product_id
                continue

            for i in range(2, half_length + 1):
                if len(str_id) % i != 0:
                    continue
                if str_id[:i] * (len(str_id) // i) == str_id:
                    invalid_register[(len(str_id) // i)] += product_id
                    break

    return invalid_register[2], sum(invalid_register.values())
