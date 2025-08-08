"""
Advent of Code - Year 2023 - Day 1
https://adventofcode.com/2023/day/1
"""

from collections.abc import Iterator
import regex as re


def preprocessing(puzzle_input: str
                  ) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    """
    Processes the puzzle input into a list of lists of integers by matching patterns using an
    automaton.
    """
    spelled_out = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits = []
    spelled = []

    for line in puzzle_input.splitlines():
        matches = [(d.start(), int(d.group())) for d in re.finditer(r'\d', line)]
        digits.append(matches.copy())

        for match in re.finditer(r'(' + '|'.join(spelled_out) + ')', line, overlapped=True):
            matches.append((match.start(), 1 + spelled_out.index(match.group())))
        spelled.append(matches)

    return digits, spelled


def solver(digits: list[list[tuple[int, int]]], spelled: list[list[tuple[int, int]]]
           ) -> Iterator[int]:
    """
    Computes two sums from a list of lists of integers: one using only single-digit numbers and one
    using all numbers, by combining the first and last digits of each sublist.
    """
    for document in (digits, spelled):
        sum_calibration = 0
        for line in document:
            sum_calibration += 10 * min(line)[1] + max(line)[1]
        yield sum_calibration
