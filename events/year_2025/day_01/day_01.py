"""
Advent of Code - Year 2025 - Day 1
https://adventofcode.com/2025/day/1
"""


def preprocessing(puzzle_input: str) -> list[int]:
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
    Solves both parts of the puzzle.
    Returns a tuple (part1_result, part2_result).
    """
    rotation = 50
    zero_cnt = 0
    pass_cnt = 0

    for instruction in instructions:
        if rotation == 0 and instruction < 0:
            rotation = 100

        rotation += instruction
        pass_cnt += abs(rotation // 100)
        rotation %= 100

        if rotation == 0:
            if instruction < 0:
                pass_cnt += 1
            zero_cnt += 1

    return zero_cnt, pass_cnt
