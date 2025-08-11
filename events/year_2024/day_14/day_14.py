"""
Advent of Code - Year 2024 - Day 14
https://adventofcode.com/2024/day/14
"""

# Standard immports
from math import prod

# First party imports
from pythonfw.functions import extract_chunks, sign


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Preprocesses the puzzle input by extracting chunks of 4 elements as lists of integers.
    """
    return extract_chunks(puzzle_input, 4)


def solver(robots: list[list[int]], w: int = 101, h: int = 103):
    """
    Simulates robot movements on a grid and yields specific metrics based on row and column
    occupancy over time.
    """
    seconds = 1
    found = (w < 31 or h < 33)

    while seconds <= 100 or not found:
        new_robots = []
        columns = {y: 0 for y in range(h)}
        rows = {x: 0 for x in range(w)}

        for px, py, vx, vy in robots:
            px = (px + vx) % w
            py = (py + vy) % h
            new_robots.append((px, py, vx, vy))
            rows[px] += 1
            columns[py] += 1

        if not found:
            if max(rows.values()) > 31 and max(columns.values()) > 33:
                yield seconds
                found = True
        robots = new_robots

        if seconds == 100:
            yield safety_factor(robots, w, h)

        seconds += 1


def safety_factor(robots: list[list[int]], w: int = 101, h: int = 103):
    """
    Given a list of robots, we sort them according to the quadrant they belong to.
    """
    quadrants = {(-1, -1): 0, (1, -1): 0, (-1, 1): 0, (1, 1): 0}
    for x, y, _, _ in robots:
        if x != (w // 2) and y != (h // 2):
            quadrants[sign(x, w // 2), sign(y, h // 2)] += 1
    return prod(quadrants.values())
