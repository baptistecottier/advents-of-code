"""
Advent of Code - Year 2021 - Day 2
https://adventofcode.com/2021/day/2
"""


def preprocessing(puzzle_input: str) -> list[tuple[int, int]]:
    """
    Parses a multiline string of movement commands into a list of (horizontal, vertical) step
    tuples.
    """
    commands = []
    for command in puzzle_input.splitlines():
        direction, steps = command.split(' ')
        match direction:
            case 'forward':
                commands.append((int(steps), 0))
            case 'up':
                commands.append((0, -int(steps)))
            case 'down':
                commands.append((0, int(steps)))
    return commands


def solver(commands: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Processes a list of movement commands and yields two computed results based on different
    movement rules.
    """
    x, y, y_aim, aim = 0, 0, 0, 0

    for dx, dy in commands:
        x += dx
        y += dy
        aim += dy
        y_aim += dx * aim

    return (x * y, x * y_aim)
