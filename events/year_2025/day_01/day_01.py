"""
Advent of Code - Year 2025 - Day 1
https://adventofcode.com/2025/day/1
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts puzzle input into a list of signed integers based on rotation direction.
    """

    instructions: list[int] = []
    for line in puzzle_input.splitlines():
        way, clicks = line[0], int(line[1:])
        if way == 'R':
            instructions.append(clicks)
        else:
            instructions.append(-clicks)

    return instructions


def solver(instructions: list[int]) -> tuple[int, int]:
    """
    Solves the puzzle by processing a list of integer instructions and 
    returns the counts of times the dial is left pointing at 0 after any rotation in the sequence 
    and then counts of time the dial points at 0.
    """

    rotation = 50
    pass_cnt = 0
    stop_cnt = 0

    for instruction in instructions:
        if rotation == 0 and instruction < 0:
            rotation = 100

        rotation += instruction
        pass_cnt += abs(abs(rotation) // 100)
        rotation %= 100

        if rotation == 0:
            if instruction < 0:
                pass_cnt += 1
            stop_cnt += 1

    return stop_cnt, pass_cnt
