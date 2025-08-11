"""
Advent of Code - Year 2024 - Day 18
https://adventofcode.com/2024/day/18
"""

from collections import deque


def preprocessing(puzzle_input: str) -> list[tuple[int, int]]:
    """
    Simply retrieves the coordinates of the falling kilobytes.
    """
    falls = []
    for coord in puzzle_input.splitlines():
        x, y = coord.split(',')
        falls.append((int(x), int(y)))
    return falls


def solver(falls: list[tuple[int, int]], size: int = 70, delay: int = 1024) -> tuple[int, str]:
    """
    Finds the minimum steps to exit given a list of falls and returns the steps and coordinates at
    a specific delay.
    """
    min_steps_to_exit = bfs(falls[:delay], size)

    left = delay
    right = len(falls)
    while right - left > 1:
        if bfs(falls[:(left + right) // 2], size) != -1:
            left = (left + right) // 2
        else:
            right = (left + right) // 2
    x, y = falls[left]
    return min_steps_to_exit, f"{x},{y}"


def bfs(maze: list[tuple[int, int]], size: int) -> int:
    """
    Finds the shortest path length from (0, 0) to (size, size) in a grid, avoiding positions in the
    maze.
    """
    queue = deque([[(0, 0)]])
    seen = set([(0, 0)])

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == (size, size):
            return len(path)-1
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if all((
                    (x2, y2) not in seen,
                    (x2, y2) not in maze,
                    0 <= x2 <= size,
                    0 <= y2 <= size)):
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return -1
