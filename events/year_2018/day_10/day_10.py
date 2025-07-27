"""
Advent of Code - Year 2018 - Day 10
https://adventofcode.com/2018/day/10
"""

from pythonfw.classes import Particule2D
from pythonfw.functions import extract_chunks, screen_reader


def preprocessing(puzzle_input: str) -> set[Particule2D]:
    """
    Parse puzzle input and return a set of 2D particles with positions and velocities.
    """
    particules = {Particule2D((x, y), (vx, vy)) for x, y, vx, vy in extract_chunks(puzzle_input, 4)}
    return particules


def solver(particules: set[Particule2D]) -> tuple[str, int]:
    """
    Simulate particle movement until they converge into a readable message.

    Moves particles over time until their vertical spread is minimal (< 10 units),
    indicating they've formed a readable pattern. Returns the decoded message and
    time elapsed.

    Args:
        particules: Set of Particule2D objects with position and velocity

    Returns:
        tuple[str, int]: (decoded_message, elapsed_seconds)
    """
    seconds = 0
    while True:
        seconds += 1
        for particule in particules:
            particule.move()
        lst_y = {particule.pos.y for particule in particules}
        min_y = min(lst_y)
        max_y = max(lst_y)
        if max_y - min_y < 10:
            break

    positions = set(particule.xy() for particule in particules)
    return screen_reader(positions), seconds
