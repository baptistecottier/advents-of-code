"""
Advent of Code - Year 2024 - Day 10
https://adventofcode.com/2024/day/10
"""

from collections import deque, defaultdict


def preprocessing(puzzle_input: str) -> tuple[list[list[int]], set[tuple[int, int]], int, int]:
    """
    Parses the puzzle input into a topographic map, a set of start positions, and the map's width
    and height.
    """
    topographic_map = []
    starts = set()
    x = y = -1

    for y, line in enumerate(puzzle_input.splitlines()):
        longitude = []
        for x, c in enumerate(line):
            if c == '0':
                starts.add((x, y))
            longitude.append(int(c))
        topographic_map.append(longitude)

    return topographic_map, starts, x + 1, y + 1


def solver(topo_map: list[list[int]], starts: set[tuple[int, int]], width: int, height: int
           ) -> tuple[int, int]:
    """
    Calculates the total number of reachable points and distinct trails from given start positions
    on a topographical map.
    """
    reachable_points = 0
    distinct_trails = 0

    for (x, y) in starts:
        hiking_trails = explore_map(topo_map, (x, y), width, height)
        reachable_points += len(hiking_trails)
        distinct_trails += sum(hiking_trails.values())

    return reachable_points, distinct_trails


def explore_map(maze: list[list[int]], start: tuple[int, int], width: int, height: int
                ) -> dict[tuple[int, int], int]:
    """
    Explores the maze from the starting position and returns a dictionary of hiking trail endpoints
    reached with their counts.
    """
    ongoing_trails = deque([start])
    hiking_trails = defaultdict(int)

    while ongoing_trails:
        x, y = ongoing_trails.popleft()
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (0 <= x2 < width and 0 <= y2 < height):
                if maze[y2][x2] == maze[y][x] + 1:
                    if maze[y2][x2] == 9:
                        hiking_trails[(x2, y2)] += 1
                    else:
                        ongoing_trails.append((x2, y2))

    return hiking_trails
