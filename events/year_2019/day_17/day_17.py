"""
Advent of Code - Year 2019 - Day 17
https://adventofcode.com/2019/day/17
"""

# Standard imports
from collections.abc import Iterator

# First party imports
from pythonfw.classes import Particule2D
from events.year_2019.ship_computer import Program


def get_functions(path):
    """
    Splits the given path into three movement functions A, B, and C.
    """
    for a in range(3, 21):
        func_a = path[:a]
        remaining = path.replace(func_a, '').replace(",,", ",").strip(",")
        if not remaining or remaining[0] not in 'LR':
            continue

        for b in range(3, 21):
            func_b = remaining[:b]
            remaining2 = remaining.replace(func_b, '').strip(",")
            if not remaining2 or remaining2[0] not in 'LR':
                continue

            for c in range(3, 21):
                func_c = remaining2[:c]
                if remaining2.replace(func_c, '').replace(',', '') == "":
                    return func_a, func_b, func_c
    raise ValueError("Impossible to split in three functions")


def get_robot_path(robot, scaffold):
    """
    Generates a path string for a robot navigating through a scaffold structure. The function moves
    the robot forward as long as possible, counting steps and recording the number of moves. When
    the robot can't move forward, it attempts to turn left or right to find a new direction The
    path is encoded as a string containing move counts and turn directions (L for left R for
    right) separated by commas. The function  continues until no valid moves areavailable and
    returns the complete path with the initial comma-separated prefix removed.
    """
    path = ""
    n = 1

    while True:
        while robot.move_in_path(scaffold):
            robot.move()
            n += 1
        path += str(n)
        n = 1

        robot.rotate_left()
        if robot.move_in_path(scaffold):
            path += ",L,"
        else:
            robot.reverse()
            if robot.move_in_path(scaffold):
                path += ",R,"
            else:
                break
        robot.move()
    return path[2:]


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a comma-separated string of integers into a list of integers.
    """
    return [int(x) for x in puzzle_input.split(',')]


def solver(intcode: list[int]) -> Iterator[int]:
    """
    This function first runs an intcode program to map out a scaffold structure and locate a robot,
    then calculates the sum of alignment parameters for intersection points. For part two, it
    generates a path for the robot to traverse the entire scaffold, splits this path into three
    reusable movement functions (A, B, C), and runs a modified intcode program to execute the
    movement routine and collect dust.
    """
    program = Program(intcode)
    scaffold, x, y, robot = set(), 0, 0, None

    while (output := program.run()) >= 0:
        match output:
            case 10:
                x, y = -1, y + 1
            case 35:
                scaffold.add((x, y))
            case 46:
                pass
            case _:
                robot = Particule2D(
                    (x, y),
                    {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}[chr(output)])
        x += 1
    if robot is None:
        raise ValueError("No robot found!")

    sum_alignment_parameters = 0
    for x, y in scaffold:
        if all((x + dx, y + dy) in scaffold
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
            sum_alignment_parameters += x * y
    yield sum_alignment_parameters

    path = get_robot_path(robot, scaffold)

    func_a, func_b, func_c = get_functions(path)
    main_routine = path.replace(func_a, "A").replace(func_b, "B").replace(func_c, "C")

    ascii_input = [ord(c) for c in "\n".join([main_routine, func_a, func_b, func_c, 'n']) + '\n']
    program = Program([2] + intcode[1:], inputs=ascii_input)

    while (output := program.run()) < 255:
        pass
    yield output
