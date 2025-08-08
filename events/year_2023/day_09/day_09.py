"""
Advent of Code - Year 2023 - Day 9
https://adventofcode.com/2023/day/9
"""

from itertools import pairwise


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Converts a multiline string of space-separated integers into a list of lists of integers.
    """
    stories = []
    for line in puzzle_input.splitlines():
        stories.append(list(map(int, line.split())))
    return stories


def solver(stories: list[list[int]]) -> tuple[int, int]:
    """
    Calculates and returns the sum of extrapolated ending and beginning values for each sequence in
    stories.
    """
    beginning = 0
    ending = 0

    for story in stories:
        ending += story[-1]
        beginning += story[0]
        flip = -1
        while not all(n == 0 for n in story):
            story = [b - a for a, b in pairwise(story)]
            ending += story[-1]
            beginning += flip * story[0]
            flip = -flip

    return ending, beginning
