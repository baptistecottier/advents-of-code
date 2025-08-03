"""
Advent of Code - Year 2020 - Day 10
https://adventofcode.com/2020/day/10
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a string of newline-separated integers into a sorted list of joltages, prepending 0
    and appending the maximum plus 3.
    """
    joltages = sorted(int(item) for item in sorted(puzzle_input.splitlines()))
    return [0] + joltages + [joltages[-1] + 3]


def solver(joltages: list[int]) -> tuple[int, int]:
    """
    Calculates the product of the counts of 1-jolt and 3-jolt differences and the total number of
    valid arrangements for a list of joltages.
    """
    differences = [b - a for a, b in zip(joltages[:-1], joltages[1:])]
    answer = differences.count(3) * differences.count(1)

    groups = 1
    while differences:
        size = 0
        while differences and differences.pop() == 1:
            size += 1
        if size > 1:
            groups *= (2 ** (size - 1) - (size == 4))
    return answer, groups
