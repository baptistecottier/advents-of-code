"""
Advent of Code - Year 2018 - Day 17
https://adventofcode.com/2018/day/17
"""

# Standard imports
import re
import os


def preprocessing(puzzle_input: str):
    """
    Parse puzzle input to extract clay vein coordinates and return as a set of (x, y) positions.
    """
    clay = set()
    for vein in puzzle_input.splitlines():
        axis, start, end = map(int, re.findall(r'\d+', vein))
        if vein.startswith('x'):
            for y in range(start, end + 1):
                clay.add((axis, y))
        else:
            for x in range(start, end + 1):
                clay.add((x, axis))
    draw(clay, "./events/year_2018/day_17/plain_ground.txt")
    if not os.path.exists("./events/year_2018/day_17/rehydrated_ground.txt"):
        with open("./events/year_2018/day_17/rehydrated_ground.txt", "w", encoding="utf-8") as fh:
            fh.write("")
    print("Ground drawed in 'plain_ground.txt'. If not existing before, a file named",
          "'rehydrated_ground.txt' also has been created. \nIt won't be replaced in further calls.")
    input("Press Enter when you have finished the simulation in 'rehydrated_ground'.txt'")
    return True


def solver(filled) -> tuple[int, int]:
    """
    Retrieve manual filling data to solve the puzzles.
    """
    if not filled:
        return 0, 0
    with open("./events/year_2018/day_17/rehydrated_ground.txt", encoding="utf-8") as file:
        content = file.read()
        rest = content.count('~')
        hypo = content.count('|')
    return (rest + hypo, rest)


def draw(clay: set[tuple[int, int]], filename: str) -> None:
    """
    Prints a visual representation of clay positions using '#' for clay and '.' for empty space.
    """
    min_depth = min(y for (_, y) in clay)
    max_depth = max(y for (_, y) in clay)
    max_width = max(x for (x, _) in clay)
    min_width = min(x for (x, _) in clay)
    content = " " * (500-min_width) + '+' + ' ' * (max_width - 500) + '\n'
    for y in range(min_depth, max_depth + 1):
        line = ""
        for x in range(min_width, max_width + 1):
            if (x, y) in clay:
                line += '#'
            else:
                line += ' '
        content += line + '\n'
    with open(filename, 'w', encoding='utf-8') as fh:
        fh.write(content)
