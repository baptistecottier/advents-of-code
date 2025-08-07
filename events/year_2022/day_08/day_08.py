"""
Advent of Code - Year 2022 - Day 8
https://adventofcode.com/2022/day/8
"""

from itertools import product


def preprocessing(puzzle_input: str) -> tuple[list[list[str]], int, int]:
    """
    Converts the puzzle input string into a 2D list of tree heights, where each height is a string.
    """
    trees = []
    x = y = 0
    for x, row in enumerate(puzzle_input.splitlines()):
        heights = []
        for y, height in enumerate(row):
            heights.append(height)
        trees.append(heights)
    return trees, x + 1, y + 1


def solver(trees: list[list[str]], width: int, depth: int) -> tuple[int, int]:
    """
    Calculates the number of visible trees and the maximum scenic score in a grid of tree heights.
    """
    visible = set()
    max_scenic = 0

    for x, y in product(range(1, depth - 1), range(1, width - 1)):
        scenic = 1
        height = trees[y][x]
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nb_trees = 1
            tx, ty = x + dx, y + dy
            while trees[ty][tx] < height:
                if (tx := tx + dx) in [-1, width] or (ty := ty + dy) in [-1, depth]:
                    visible.add((x, y))
                    break
                nb_trees += 1
            scenic *= nb_trees
        max_scenic = max(max_scenic, scenic)

    return 2 * (width + depth - 2) + len(visible), max_scenic
