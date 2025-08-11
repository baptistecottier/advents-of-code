"""
Advent of Code - Year 2024 - Day 20
https://adventofcode.com/2024/day/20
"""

from collections import deque, defaultdict


def preprocessing(puzzle_input: str
                  ) -> tuple[set[tuple[int, int]], tuple[int, int], tuple[int, int]]:
    """
    Parses the puzzle input and returns the set of wall coordinates, start position, and end
    position.
    """
    walls = set()
    start = end = (-1, -1)

    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                walls.add((x, y))
            if c == 'S':
                start = (x, y)
            elif c == 'E':
                end = (x, y)
    return walls, start, end


def solver(walls: set[tuple[int, int]],
           start: tuple[int, int],
           end: tuple[int, int],
           ) -> tuple[int, int]:
    """
    Analyzes a path through walls from start to end and yields counts of small and long path-saving
    shortcuts based on specified minimum savings.
    """

    classical_path = bfs(walls, start, end)
    length = len(classical_path)
    long_cheats = defaultdict(int)
    small_cheats = defaultdict(int)
    min_saved_ps = [100, 100]

    for i, (xa, ya) in enumerate(classical_path):
        for j in range(i + min_saved_ps[0], length):
            xb, yb = classical_path[j]
            m = abs(yb - ya) + abs(xb - xa)
            if j - i - m >= min_saved_ps[0] and m < 21:
                if j - i - m >= min_saved_ps[1]:
                    long_cheats[j - i - m] += 1
                if m < 3:
                    small_cheats[j - i - m] += 1

    return sum(small_cheats.values()), sum(long_cheats.values())


def bfs(walls: set[tuple[int, int]], start: tuple[int, int], end: tuple[int, int]
        ) -> list[tuple[int, int]]:
    """
    Finds the shortest path from start to end on a grid, avoiding walls, using breadth-first search.
    """
    queue = deque([[start]])
    seen = set([start])

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) not in seen and (x2, y2) not in walls:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

    raise ValueError("No path to the end found!")
