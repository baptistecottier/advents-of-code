"""
Advent of Code - Year 2022 - Day 13
https://adventofcode.com/2022/day/13
"""

# Standard imports
from ast import literal_eval
from functools import cmp_to_key
from typing import Any

# First party imports
from pythonfw.functions import sign


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Converts a puzzle input string into a list of lists of integers by evaluating each line.
    """
    list_input = [literal_eval(line) for line in puzzle_input.replace('\n\n', '\n').splitlines()]
    return list_input


def solver(packets: list[Any]) -> tuple[int, int]:
    """
    Solves the packet ordering puzzle by computing the sum of ordered pairs and the product of
    special packet indices.
    """
    orders = [((i + 1) * is_pair_sorted(packets[2 * i], packets[2 * i + 1]))
              for i in range(len(packets)//2)]

    packets = sorted(
        packets + [[2], [6]],
        key=cmp_to_key(lambda x, y: sign(x, y, is_pair_sorted)),
        reverse=True)

    return sum(orders), (packets.index([2]) + 1) * (packets.index([6]) + 1)


def is_pair_sorted(a: int | list, b: int | list) -> bool:
    """
    Recursively determines if two elements (integers or nested lists) are sorted in ascending order
    according to custom comparison rules.
    """
    if isinstance(a, int) and isinstance(b, int):
        return a < b
    if isinstance(a, list) and isinstance(b, list):
        if a == []:
            return True
        if b == []:
            return False
        if a[0] == b[0]:
            a, b = a[1:], b[1:]
        else:
            a, b = a[0], b[0]
    elif isinstance(a, list) and isinstance(b, int):
        b = [b]
    elif isinstance(a, int) and isinstance(b, list):
        a = [a]
    return is_pair_sorted(a, b)
