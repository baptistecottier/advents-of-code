"""
Advent of Code - Year 2020 - Day 12
https://adventofcode.com/2020/day/12
"""

from pythonfw.classes import Particule2D


def preprocessing(puzzle_input: str) -> list[tuple[str, int]]:
    """
    Parses the input string into a list of (action, value) tuples, where action is a character and
    value is an integer.
    """
    return list(map(lambda x: (x[0], int(x[1:])), puzzle_input.splitlines()))


def solver(instructions: list[tuple[str, int]]) -> tuple[int, int]:
    """
    Solves two navigation problems using the provided list of instructions and returns their
    respective results as a tuple.
    """
    return (navigate(instructions, (1, 0), "pos"),
            navigate(instructions, (10, 1), "vel"))


def navigate(instructions: list[tuple[str, int]], velocity: tuple[int, int], attr: str) -> int:
    """
    Executes a sequence of navigation instructions on a 2D particle, updating its position and
    orientation, and returns the Manhattan distance from the origin.
    """
    ferry = Particule2D(v=velocity)

    for act, val in instructions:
        tx, ty = 0, 0
        match act:
            case 'N': ty = val
            case 'S': ty = -val
            case 'E': tx = val
            case 'W': tx = -val
            case 'L':
                for _ in range(val // 90):
                    ferry.rotate_left()
            case 'R':
                for _ in range(val // 90):
                    ferry.rotate_right()
            case 'F':
                for _ in range(val):
                    ferry.move()
        getattr(ferry, attr).x += tx
        getattr(ferry, attr).y += ty

    return ferry.pos.manhattan()
