"""
Advent of Code - Year 2024 - Day 1
https://adventofcode.com/2024/day/1
"""


def preprocessing(puzzle_input: str) -> tuple[list[int], list[int]]:
    """
    Splits the input string into integers, sorts even-indexed and odd-indexed numbers separately,
    and returns them as two lists.
    """
    numbers = [int(item) for item in puzzle_input.split()]
    return sorted(numbers[::2]), sorted(numbers[1::2])


def solver(left_list: list[int], right_list: list[int]) -> tuple[int, int]:
    """
    Calculates the sum of absolute differences between paired elements and the sum of occurrences
    of each element in the right_list list multiplied by its value from the left_list list.
    """
    return (sum(abs(left - right) for left, right in zip(left_list, right_list)),
            sum(left * right_list.count(left) for left in left_list))
