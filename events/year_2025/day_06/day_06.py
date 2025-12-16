"""
Advent of Code - Year 2025 - Day 6
https://adventofcode.com/2025/day/6
"""

from math import prod
from collections.abc import Callable


def preprocessing(puzzle_input: str) -> list[tuple[list[list[str]], Callable]]:
    """
    Returns a list of tuples where each tuple contains a matrix of digits and its operation
    function.
    """
    lines = puzzle_input.splitlines()
    op = lines[-1].split()
    problems = []
    problem = [[] for _ in range(len(lines) - 1)]
    for i in range(len(lines[0])):
        if all(line[i] == ' ' for line in lines):
            problems.append((problem, sum if op.pop(0) == '+' else prod))
            problem = [[] for _ in range(len(lines) - 1)]
        else:
            for j in range(len(lines) - 1):
                problem[j] += lines[j][i]
    problems.append((problem, sum if op.pop(0) == '+' else prod))
    return problems


def solver(problems: list[tuple[list[list[str]], Callable]]) -> tuple[int, int]:
    """
    Calculates horizontal and vertical sums by applying operations to problem data.
    Returns a tuple containing the total horizontal and vertical results.
    """
    horizontal = 0
    vertical = 0
    for problem, op in problems:
        horizontal += op(int("".join(line)) for line in problem)
        vertical += op(int("".join(line)) for line in list(map(list, zip(*problem))))

    return horizontal, vertical
