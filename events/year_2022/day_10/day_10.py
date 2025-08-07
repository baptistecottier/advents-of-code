"""
Advent of Code - Year 2022 - Day 10
https://adventofcode.com/2022/day/10
"""

from pythonfw.functions import screen_reader


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a puzzle input string into a list of integers representing instructions for further
    processing.
    """
    instructions = []
    for instruction in puzzle_input.splitlines():
        instructions.append(0)
        if 'addx' in instruction:
            instructions.append(int(instruction.split(' ')[1]))
    return instructions


def solver(instructions: list[int]) -> tuple[int, str]:
    """
    Processes a list of integer instructions to compute signal strength and generate a visual
    display representation.
    """
    x = 1
    strength = 0
    display = set()

    for i, shift in enumerate(instructions):
        if (i - 19) % 40 == 0:
            strength += (i + 1) * x
        if i % 40 in (x - 1, x, x + 1):
            display.add((i % 40, i // 40))
        x += shift

    return strength, screen_reader(display)
