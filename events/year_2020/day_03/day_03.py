"""
Advent of Code - Year 2020 - Day 3
https://adventofcode.com/2020/day/3
"""

from pythonfw.classes import Particule2D


def preprocessing(puzzle_input: str) -> tuple[set, int, int]:
    """
    Parses the puzzle input and returns a set of tree coordinates along with the map's width and
    height.
    """
    trees = set()
    x = y = 0
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            if c == '#':
                trees.add((x, y))
    return trees, x + 1, y


def solver(trees: set, width: int, height: int) -> tuple[int, int]:
    """
    Counts the number of trees encountered for different slopes on a map and returns the count for
    the last slope and the sum of all counts.
    """
    counts = []
    for dx, dy in ((1, 1), (5, 1), (7, 1), (1, 2), (3, 1)):
        me = Particule2D(v=(dx, dy))
        cnt = 0
        while me.pos.y <= height:
            if (me.pos.x % width, me.pos.y) in trees:
                cnt += 1
            me.move()
        counts.append(cnt)
    return counts[-1], sum(counts)
