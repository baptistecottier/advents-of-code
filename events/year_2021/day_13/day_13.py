"""
Advent of Code - Year 2021 - Day 8
https://adventofcode.com/2021/day/8
"""

from pythonfw.functions import screen_reader


def preprocessing(puzzle_input: str) -> tuple[set[tuple[int, ...]], list[tuple[str, int]]]:
    """
    Parses the puzzle input into a set of dot coordinates and a list of fold instructions.
    """
    dots_str, folds_str = puzzle_input.split('\n\n')
    dots = {tuple(map(int, dot.split(','))) for dot in dots_str.splitlines()}
    folds = [(fold[11], int(fold[13:])) for fold in folds_str.splitlines()]
    return dots, folds


def solver(dots: set[tuple[int, ...]], folds: list[tuple[str, int]]) -> tuple[int, str]:
    """
    Processes a set of dot coordinates and a list of fold instructions, yielding the number of
    visible dots after the first fold and the final screen representation.
    """
    length_after_first_fold = -1
    for k, (axis, n) in enumerate(folds):
        if axis == 'x':
            dots = {(min(x, 2 * n - x), y) for (x, y) in dots}
        if axis == 'y':
            dots = {(x, min(y, 2 * n - y)) for (x, y) in dots}
        if k == 0:
            length_after_first_fold = len(dots)

    return length_after_first_fold, screen_reader(dots)
