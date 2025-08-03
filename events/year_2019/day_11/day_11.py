"""
Advent of Code - Year 2019 - Day 11
https://adventofcode.com/2019/day/11
"""

# First party imports
from pythonfw.classes import Particule2D
from pythonfw.functions import screen_reader
from events.year_2019.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a comma-separated string of integers into a list of integers.
    """
    return list(map(int, puzzle_input.split(',')))


def solver(intcode: list[int]) -> tuple[int, str]:
    """
    Solves the painting robot puzzle by running the Intcode program and returns the number of
    panels painted at least once and the registration identifier as a string.
    """
    _, whited = paint(intcode, set())
    white, _ = paint(intcode, {(0, 0)})
    return len(whited), screen_reader(white)


def paint(intcode: list[int], white: set) -> tuple[set, set]:
    """
    Simulates a painting robot on a grid using an Intcode program, updating the set of white panels
    and tracking painted panels.
    """
    whited = set()
    robot = Particule2D(v=(0, -1))
    painter: Program = Program(intcode)

    while not painter.halt:
        color = int(robot.xy() in white)
        match painter.run(color), color:
            case 1, 0:
                white.add(robot.xy())
                whited.add(robot.xy())
            case 0, 1:
                white.remove(robot.xy())
        if painter.run(color):
            robot.rotate_right()
        else:
            robot.rotate_left()
        robot.move()

    return white, whited
