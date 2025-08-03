"""
Advent of Code - Year 2019 - Day 4
https://adventofcode.com/2019/day/4
"""

from collections import Counter
from itertools import pairwise


def preprocessing(puzzle_input: str) -> tuple[int, int]:
    """
    Converts a hyphen-separated string of numbers into a tuple of integers.
    """
    min_bound, max_bound = puzzle_input.split('-', maxsplit=2)
    return int(min_bound), int(max_bound)


def solver(b_min: int, b_max: int) -> tuple[int, int]:
    """
    Counts the number of passwords within the given range that meet specific criteria for
    increasing digits and repeated digits.
    """
    cnt_eq = 0
    cnt_ge = 0

    for pw in range(b_min, b_max + 1):
        if all(a <= b for (a, b) in pairwise(str(pw))):
            values = [n for (_, n) in Counter(str(pw)).most_common() if n > 1]
            if values:
                cnt_ge += 1
            if 2 in values:
                cnt_eq += 1

    return cnt_ge, cnt_eq
