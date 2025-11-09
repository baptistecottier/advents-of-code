"""
Advent of Code - Year 2020 - Day 6
https://adventofcode.com/2020/day/6
"""

from collections import Counter
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[list[str]]:
    """
    Splits the input string into groups separated by double newlines and returns each group as a
    list of lines.
    """
    return [group.splitlines() for group in puzzle_input.split('\n\n')]


def solver(groups: Iterator[list[str]]) -> tuple[int, int]:
    """
    Calculates the total number of questions answered 'yes' by anyone and by everyone in each group
    from an iterator of groups of answers.
    """
    anyone = 0
    everyone = 0

    for group in groups:
        answers = tuple(c for _, c in Counter(''.join(group)).most_common() if c >= 1)
        anyone += len(answers)
        everyone += len(tuple(answer for answer in answers if answer == len(group)))

    return anyone, everyone
