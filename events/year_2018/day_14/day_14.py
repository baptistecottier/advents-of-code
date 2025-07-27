"""
Advent of Code - Year 2018 - Day 14
https://adventofcode.com/2018/day/14
"""


def preprocessing(puzzle_input: str) -> tuple[list[int], int]:
    """
    Converts puzzle input string to a list of individual digits and an integer.
    """
    return list(int(n) for n in puzzle_input), int(puzzle_input)


def solver(pattern: list[int], length: int) -> tuple[str, int]:
    """
    Simulates recipe generation by two elves until a specific pattern is found.

    Args:
        pattern: List of integers representing the target pattern to find
        length: Integer used to calculate trigger point for result extraction

    Returns:
        Tuple containing:
        - String of 10 recipes starting from (length) position
        - Integer position where pattern was found in the recipe list

    Examples:
        >>> solver([5, 1, 5, 8, 9], 9)
        ('5158916779', 9)
        >>> solver([0, 1, 2, 4, 5], 18)
        ('9251071085', 5)
    """
    elves = (0, 1)
    recipes = [3, 7]
    trigger = length + 10

    while True:
        s = sum(recipes[e] for e in elves)
        if s > 9:
            recipes.append(s // 10)
        recipes.append(s % 10)
        elves = list((e + recipes[e] + 1) % len(recipes) for e in elves)

        if recipes[-6:] == pattern:
            return ''.join(str(n) for n in recipes[trigger - 10: trigger]), len(recipes) - 6

        if recipes[-7:-1] == pattern:
            return ''.join(str(n) for n in recipes[trigger - 10: trigger]), len(recipes) - 7
