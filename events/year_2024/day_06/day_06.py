"""
Advent of Code - Year 2024 - Day 6
https://adventofcode.com/2024/day/6
"""


def preprocessing(puzzle_input: str
                  ) -> tuple[tuple[int, int], set[tuple[int, int]], int, int]:
    """
    Preprocessing consists in retrieving all obstacles location and the guard position.
    """
    guard = None
    obstacles = set()
    x = y = -1
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == '^':
                guard = (x, y)
            elif c == '#':
                obstacles.add((x, y))
    if guard is None:
        raise ValueError("No guard position found in the input.")
    return (guard, obstacles, x, y)


def solver(guard: tuple[int, int], obstacles: set[tuple[int, int]], width: int, height: int
           ) -> tuple[int, int]:
    """
    Simulates a guard's patrol through a grid with obstacles and yields the number of visited
    positions and obstructed positions causing patrol loops.
    """
    obstructions = set()
    gx, gy = guard
    dx, dy = (0, -1)
    visited = set()

    while 0 <= gx < width and 0 <= gy < height:

        while (gx + dx, gy + dy) in obstacles:
            dx, dy = (dy if dx else - dy, dx)
        obstacle = (gx + dx, gy + dy)

        if obstacle in visited:
            start = (guard, ((0, -1)))
        else:
            start = ((gx, gy), (dx, dy))

        if is_patrol_looping(start, obstacles.union([obstacle]), width, height):
            obstructions.add(obstacle)
        visited.add(((gx, gy)))
        gx, gy = obstacle

    return len(visited), len(obstructions)


def is_patrol_looping(start: tuple[tuple[int, int], tuple[int, int]],
                      obstacles: set[tuple[int, int]],
                      width: int,
                      height: int
                      ) -> bool:
    """
    Determines whether a patrol starting at a given position and direction loops indefinitely
    within the grid, considering obstacles.
    """
    (gx, gy), (dx, dy) = start
    visited = set()

    while 0 <= gx <= width and 0 <= gy <= height:
        if ((dx, dy), (gx, gy)) in visited:
            return True

        visited.add(((dx, dy), (gx, gy)))
        while (gx + dx, gy + dy) in obstacles:
            dx, dy = (dy if dx else - dy, dx)
        gx, gy = gx + dx, gy + dy

    return False
