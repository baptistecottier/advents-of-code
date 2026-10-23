"""
Advent of Code - Year 2021 - Day 18
https://adventofcode.com/2021/day/18
"""

# Standard imports
from collections.abc import Iterator
from itertools import permutations
from json import loads
import re


type Snailfish = int | list[Snailfish]


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Splits the puzzle input into one snailfish number per line.
    """
    return puzzle_input.splitlines()


def solver(lines: list[str]) -> Iterator[int]:
    """
    Yields the magnitude of the sum of all snailfish numbers, then the largest magnitude of the sum
    of any two different numbers.
    """
    snailfish = lines[0]
    for sf_b in lines[1:]:
        snailfish = sum_sf(snailfish, sf_b)
    snailfish_as_list = loads(snailfish)
    yield magnitude(snailfish_as_list)

    max_magnitude = 0
    for sf_a, sf_b in permutations(lines, 2):
        max_magnitude = max(
            max_magnitude,
            magnitude(loads(sum_sf(sf_a, sf_b))))
    yield max_magnitude


def sum_sf(sf_a: str, sf_b: str) -> str:
    """
    Adds two snailfish numbers and reduces the result.
    """
    snailfish = f"[{sf_a},{sf_b}]"
    return update(snailfish)


def update(snailfish: str) -> str:
    """
    Reduces a snailfish number: explodes, then splits, until no action applies.
    """
    while True:
        new_sf = explode(snailfish)
        if new_sf == snailfish:
            new_sf = split(snailfish)
            if new_sf == snailfish:
                return snailfish
            snailfish = new_sf
        else:
            snailfish = new_sf


def explode(snailfish: str) -> str:
    """
    Explodes the leftmost pair nested inside four pairs, if any.
    """
    depth = 0
    i = 0
    while i < len(snailfish):
        c = snailfish[i]
        if c == '[':
            depth += 1
        if c == ']':
            depth -= 1
        if depth == 5:
            # Retrieve elements of the pair
            result = re.search(r'(\d+),(\d+)', snailfish[i:])
            if not result:
                raise ValueError("Incorrect snailfish format")
            left, right = list(map(int, result[0].split(',')))

            left_snailfish = re.sub(
                r'\d+',
                lambda m: str(int(m[0][::-1]) + left)[::-1],
                snailfish[:i][::-1],
                count=1)[::-1]
            right_snailfish = re.sub(
                r'\d+',
                lambda m: str(int(m[0]) + right),
                snailfish[i + result.end() + 1:],
                count=1)

            snailfish = left_snailfish + '0' + right_snailfish
            return snailfish
        i += 1
    return snailfish


def split(snailfish: str) -> str:
    """
    Splits the leftmost regular number of 10 or more, if any.
    """
    result = re.search(r'\d{2}', snailfish)
    if result is not None:
        value = int(result[0])
        a = value // 2
        b = value - a
        repl = f"[{a},{b}]"
        snailfish = re.sub(result[0], repl, snailfish, count=1)
    return snailfish


def magnitude(item: Snailfish) -> int:
    """
    Computes the magnitude of a snailfish number.
    """
    if isinstance(item, int):
        return item
    return 3 * magnitude(item[0]) + 2 * magnitude(item[1])
