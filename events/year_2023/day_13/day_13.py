"""
Advent of Code - Year 2023 - Day 13
https://adventofcode.com/2023/day/13
"""


def preprocessing(puzzle_input: str) -> list[tuple[dict[tuple[int, int], bool], int, int]]:
    """
    Parses the puzzle input into a list of patterns represented as dictionaries mapping coordinates
    to booleans, along with their width and height.
    """
    patterns = []
    for raw_tile in puzzle_input.split('\n\n'):
        pattern = {}
        x = y = 0
        for y, line in enumerate(raw_tile.splitlines()):
            for x, c in enumerate(line):
                pattern[(x, y)] = c == '#'
        patterns.append((pattern, x + 1, y + 1))
    return patterns


def solver(patterns: list[tuple[dict[tuple[int, int], bool], int, int]]) -> tuple[int, int]:
    """
    Calculates and returns two scores for each pattern based on symmetry checks across possible
    vertical and horizontal axes.
    """
    old = new = 0
    for pattern, w, h in patterns:
        scores = []

        for p in range(1, w):
            to_check = {(x, y) for (x, y) in pattern if x < p}
            score = sum(pattern[(x, y)] == pattern.get((2 * p - x - 1, y), pattern[(x, y)])
                        for x, y in to_check)
            scores.append((len(to_check) - score, p))

        for p in range(1, h):
            to_check = {(x, y) for (x, y) in pattern if y < p}
            score = sum(pattern[(x, y)] == pattern.get((x, 2 * p - y - 1), pattern[(x, y)])
                        for x, y in to_check)
            scores.append((len(to_check) - score, 100 * p))

        scores.sort()

        old += scores[0][1]
        new += scores[1][1]

    return old, new
