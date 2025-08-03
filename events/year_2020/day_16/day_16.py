"""
Advent of Code - Year 2020 - Day 16
https://adventofcode.com/2020/day/16
"""

# Standard imports
from itertools import chain
from math import prod

# Third party imports
from parse import parse, Result


def preprocessing(puzzle_input: str) -> tuple[list[list[chain]], list[int], list[list[int]]]:
    """
    Parses the puzzle input string into rules, your ticket, and nearby tickets as structured lists.
    """
    p_rules, p_ticket, p_nearby = puzzle_input.split('\n\n')
    rules = []

    for rule in p_rules.splitlines():
        result = parse("{}: {:d}-{:d} or {:d}-{:d}", rule)
        if not isinstance(result, Result):
            raise ValueError("Wrong input format")
        _, a, b, c, d = result
        rules.append(list(chain(range(a, b + 1), range(c, d + 1))))

    ticket = [int(item) for item in p_ticket.splitlines()[1].split(',')]
    nearby = [[int(item) for item in n.split(',')] for n in p_nearby.splitlines()[1:]]
    return rules, ticket, nearby


def solver(
        rules: list[list[chain]], ticket: list[int], nearby: list[list[int]]) -> tuple[int, int]:
    """
    Solves a ticket validation and field assignment problem, returning the sum of invalid values
    and the product of specific ticket fields.
    """
    counter, nearby = invalid_detector(rules, nearby)

    candidates = [[i for i in range(len(ticket)) if all(n[i] in r for n in nearby)] for r in rules]
    while any(len(c) != 1 for c in candidates):
        for c in candidates:
            if len(c) == 1:
                for cc in candidates:
                    if cc != c and c[0] in cc:
                        cc.remove(c[0])

    return counter, prod(ticket[candidates[i][0]] for i in range(6))


def invalid_detector(rules: list[list[chain]], nearby: list[list[int]]):
    """
    Detects and counts invalid values in nearby tickets based on provided rules, and filters out
    invalid tickets.
    """
    valid = list(chain(*rules))
    cnt = sum(sum(v for v in n if v not in valid) for n in nearby)
    nearby = [n for n in nearby if all(item in valid for item in n)]
    return cnt, nearby
