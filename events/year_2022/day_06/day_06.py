"""
Advent of Code - Year 2022 - Day 6
https://adventofcode.com/2022/day/6
"""

from collections.abc import Iterator


def solver(buffer: str) -> Iterator[int]:
    """
    Yields the ending index of the first substring of specified size(s) in the buffer with all
    unique characters.
    """
    i = 0
    for size in [4, 14]:
        while len(set(buffer[i:i + size])) != size:
            i += 1
        yield i + size
