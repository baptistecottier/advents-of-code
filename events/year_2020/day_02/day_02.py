"""
Advent of Code - Year 2020 - Day 2
https://adventofcode.com/2020/day/2
"""

from parse import parse, Result


def preprocessing(puzzle_input: str) -> list[tuple[int, int, str, str]]:
    """
    Parses the puzzle input into a list of tuples containing password policy parameters and the
    password string.
    """
    passwords = []
    for pw in puzzle_input.splitlines():
        result = parse("{:d}-{:d} {}: {}", pw)
        if isinstance(result, Result):
            passwords.append(result)
        else:
            raise ValueError("Wrong input format!")
    return passwords


def solver(passwords: list[tuple[int, int, str, str]]) -> tuple[int, int]:
    """
    Counts the number of valid passwords according to two different rules given a list of password
    policies and passwords.
    """
    old_rule = 0
    new_rule = 0

    for a, b, w, pw in passwords:
        if a <= pw.count(w) <= b:
            old_rule += 1
        if (pw[a-1] == w) ^ (pw[b-1] == w):
            new_rule += 1

    return old_rule, new_rule
