"""
Advent of Code - Year 2019 - Day 13
https://adventofcode.com/2019/day/13
"""

from pythonfw.functions import sign
from events.year_2019.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a comma-separated string of integers into a list of integers.
    """
    return list(map(int, puzzle_input.split(',')))


def solver(intcode: list[int]) -> tuple[int, int]:
    """
    Solves the arcade game puzzle by counting block tiles and calculating the final score using the
    provided Intcode program.
    """
    ball = 0
    block = 0
    score = 0
    paddle = 0

    arcade = Program(intcode)
    while not arcade.halt:
        _, _, tile_id = (arcade.run() for _ in range(3))
        if tile_id == 2:
            block += 1

    arcade = Program([2] + intcode[1:])

    while not arcade.halt:
        puzzle_input = sign(ball - paddle)
        x, _, tile_id = (arcade.run(puzzle_input) for _ in range(3))
        match (x, tile_id):
            case (-1, _):
                score = tile_id
            case (_, 3):
                paddle = x
            case (_, 4):
                ball = x
    return block, score
