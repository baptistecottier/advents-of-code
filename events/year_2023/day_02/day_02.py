"""
Advent of Code - Year 2023 - Day 2
https://adventofcode.com/2023/day/2
"""

import re


def preprocessing(puzzle_input: str) -> list[list[tuple[int, int]]]:
    """
    Parses the puzzle input string into a list of lists of tuples, each containing a number and the
    index of a color.
    """
    game = []
    for line in puzzle_input.splitlines():
        draws = [(int(n), "bgr".index(c)) for n, c in re.findall(r'([0-9]+)\s+(b|g|r)', line)]
        game.append(draws)
    return game


def solver(game: list[list[tuple[int, int]]]) -> tuple[int, int]:
    """
    Calculates and yields the sum of valid game IDs and the total power based on maximum values of
    each color in the provided game data.
    """
    power = 0
    sumid = 0
    for game_id, draws in enumerate(game, 1):
        if all(n + c < 15 for (n, c) in draws):
            sumid += game_id

        mb = max(n for (n, c) in draws if c == 0)
        mg = max(n for (n, c) in draws if c == 1)
        mr = max(n for (n, c) in draws if c == 2)
        power += mb * mg * mr

    return sumid, power
