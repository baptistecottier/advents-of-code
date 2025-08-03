"""
Advent of Code - Year 2020 - Day 25
https://adventofcode.com/2020/day/25
"""


def preprocessing(puzzle_input: str) -> tuple[int, int]:
    """
    Parses the input string and returns a tuple of two integers extracted from the first two lines.
    Any other integer will be ignored.
    """
    lines = puzzle_input.splitlines()
    p = int(lines[0])
    q = int(lines[1])
    return p, q


def solver(p: int, q: int):
    """
    Finds the encryption key by determining the loop size for one of the public keys and applying
    the transformation with the other key.
    """
    e = 0
    n = 1
    while n not in (p, q):
        n = (n * 7) % 20201227
        e += 1
    if n == p:
        yield pow(q, e, 20201227)
    if n == q:
        yield pow(p, e, 20201227)
