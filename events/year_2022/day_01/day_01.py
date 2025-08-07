"""
Advent of Code - Year 2022 - Day 1
https://adventofcode.com/2022/day/1
"""


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Converts the puzzle input string into a list of lists of integers, where each sublist
    represents the calories carried by an elf.
    """
    reeinders = [list(map(int, reeinder.splitlines())) for reeinder in puzzle_input.split("\n\n")]
    return reeinders


def solver(reeinders: list[list[int]]) -> tuple[int, int]:
    """
    Returns the maximum sum and the sum of the top three sums from a list of lists of integers.
    """
    calories = sorted([sum(reeinder) for reeinder in reeinders])
    return calories[-1], sum(calories[-3:])
