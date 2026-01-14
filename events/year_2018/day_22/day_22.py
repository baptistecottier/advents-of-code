"""
Advent of Code - Year 2018 - Day 22
https://adventofcode.com/2018/day/22
"""

from queue import PriorityQueue


def preprocessing(puzzle_input: str) -> tuple[list[list[int]], int, int]:
    """
    Parses puzzle input to calculate erosion levels for a cave system and returns the erosion grid
    with target coordinates.
    """
    depth, target = puzzle_input.splitlines()
    depth = int(depth.rsplit(' ')[1])
    tx, ty = tuple(int(n) for n in (target.split(': ')[1]).split(','))
    line = [0]

    for x in range(1, tx + 50):
        line.append((x * 16807 + depth) % 20183)
    erosion = [line]

    for y in range(1, ty + 50):
        line = [(y * 48271 + depth) % 20183]
        for x in range(1, tx + 50):
            line.append((line[x - 1] * erosion[y - 1][x] + depth) % 20183)
        erosion.append(line)

    erosion = [[item % 3 for item in y] for y in erosion]
    erosion[ty][tx] = 0
    return erosion, tx, ty


def solver(erosion: list[list[int]], tx: int, ty: int):
    """
    Calculates the sum of erosion values within a rectangular region for part 1,
    and finds the shortest path to the target for part 2.
    """
    part1 = sum(sum(y[:tx + 1]) for y in erosion[:ty + 1])
    part2 = bfs(erosion, (tx, ty))
    return part1, part2


def bfs(maze: list[list[int]], end: tuple[int, int]):
    """
    Finds the minimum time to reach the target in the maze, considering tool switching and terrain
    compatibility.
    """
    width, height = len(maze[0]), len(maze)
    queue = PriorityQueue()
    queue.put((0, 0, 0, 2))
    visited = {}

    while queue:
        time, x, y, tool = queue.get()

        if (x, y, tool) in visited:
            continue
        visited[(x, y, tool)] = time

        if (x, y) == end and tool == 2:
            return time

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < width and 0 <= ny < height):
                if is_tool_compatible(tool, maze[ny][nx]) and (nx, ny, tool) not in visited:
                    queue.put((time + 1, nx, ny, tool))

        for new_tool in range(3):
            if new_tool != tool and is_tool_compatible(new_tool, maze[y][x]):
                if (x, y, new_tool) not in visited:
                    queue.put((time + 7, x, y, new_tool))

    return -1


def is_tool_compatible(tool: int, terrain: int) -> bool:
    """
    Check if a tool can be used on a given terrain type.
    """
    if terrain == 0:  # rocky
        return tool in [1, 2]
    if terrain == 1:  # wet
        return tool in [0, 1]
    if terrain == 2:  # narrow
        return tool in [0, 2]
    return False
