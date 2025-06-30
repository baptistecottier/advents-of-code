"""Advent of Code - Year 2016 - Day 17"""

from collections import deque
from pythonfw import functions


def solver(salt: str):
    """
    Finds all possible paths and the longest path length in a 4x4 grid using a salt string.

    Yields:
        str: The first path found to the goal (excluding the salt prefix).
        int: The length of the longest path to the goal (excluding the salt prefix).
    """
    paths = deque([(salt, 0, 0)])
    longest = -1
    neighbours = [('U', 0, -1), ('D', 0, 1), ('L', -1, 0), ('R', 1, 0)]
    while paths:
        salt, x, y = paths.popleft()
        if x == y == 3:
            if longest == -1:
                yield salt[8:]
            longest = len(salt)
        else:
            md5_hash = functions.md5(salt)[:4]
            for i, (turn, dx, dy) in enumerate(neighbours):
                if 'b' <= md5_hash[i] <= 'f' and 0 <= x + dx <= 3 and 0 <= y + dy <= 3:
                    paths.append((salt + turn, x + dx, y + dy))
    yield longest - 8
