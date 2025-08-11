"""
Advent of Code - Year 2024 - Day 3
https://adventofcode.com/2024/day/3
"""

from collections.abc import Iterator
import re


def solver(program: str) -> Iterator[int]:
    """
    For the first part, scan the program for uncorrupted mul operations. Then remove all
    don't()...do() enclosure and remove the last disabled instructions following a don't()
    """
    yield scan_mul(program)

    program = re.sub(r"don\'t\(\)([\s\S]*?)do\(\)", "", program)
    program = program.split("don\'t()", 1)[0]
    yield scan_mul(program)


def scan_mul(program: str) -> int:
    """
    Use regex expression to extract uncorrupted instructions with one up to 3 digits. Then add the
    product of matched pairs and return it
    """
    score = 0
    uncorrupted = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", program)
    for a, b in uncorrupted:
        score += int(a) * int(b)
    return score
