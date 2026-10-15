"""
Advent of Code - Year 2023 - Day 23
https://adventofcode.com/2023/day/23
"""

from collections import deque
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[list[str]]:
    """
    Parses the puzzle input into a grid of characters.
    """
    grid = [list(line) for line in puzzle_input.splitlines()]
    return grid


def solver(grid: list[list[str]]) -> Iterator[int]:
    """
    Explores every hike between crossroads in a single search, labelling those that climb a
    slope, and yields the longest hike walking downhill only, then the longest hike overall.
    """
    crossroads = get_crossroads(grid)
    distances = dist_between_crossroads(crossroads, grid)

    max_dist = [0, 0]
    queue = deque([((1, 0), {(1, 0)}, 0, False)])
    end = (len(grid[0]) - 2, len(grid) - 1)
    # Only one crossroad leads to the end: once there, the hike must go straight to the end.
    (last, to_end, _), = distances[end]

    while queue:
        node, used_cr, dist, uphill = queue.pop()
        if node == last:
            max_dist[uphill] = max(dist + to_end, max_dist[uphill])
            continue
        for nxt, d, hill in distances[node]:
            if nxt not in used_cr:
                queue.append((nxt, used_cr | {nxt}, dist + d, uphill or hill))
    yield max_dist[0]
    yield max(max_dist)


def get_crossroads(grid: list[list[str]]) -> set[tuple[int, int]]:
    """
    Finds the tiles with more than two open neighbours, along with the start and the end.
    """
    h = len(grid)
    w = len(grid[0])
    crossroads = {(1, 0), (w - 2, h - 1)}
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if grid[y][x] == '#':
                continue
            cnt = 0
            for x2, y2 in ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)):
                if grid[y2][x2] != '#':
                    cnt += 1
            if cnt > 2:
                crossroads.add((x, y))
    return crossroads


def dist_between_crossroads(crossroads: set[tuple[int, int]], grid: list[list[str]]
                            ) -> dict[tuple[int, int], list[tuple[tuple[int, int], int, bool]]]:
    """
    Follows each trail leaving a crossroad downhill until the next crossroad, and records it
    in both directions as (crossroad, number of steps, whether it is walked uphill).
    """
    open_tiles = {(x, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c != '#'}
    distances = {pt: [] for pt in crossroads}
    for (x, y) in crossroads:
        for (tx, ty, s) in ((x, y - 1, '^'), (x - 1, y, '<'), (x + 1, y, '>'), (x, y + 1, 'v')):
            if (tx, ty) not in open_tiles:
                continue
            if grid[ty][tx] != s and (x, y, grid[ty][tx]) != (1, 0, '.'):
                continue
            steps = 1
            px, py = x, y
            while (tx, ty) not in crossroads:
                for (nx, ny) in ((tx, ty - 1), (tx - 1, ty), (tx + 1, ty), (tx, ty + 1)):
                    if (nx, ny) in open_tiles and (nx, ny) != (px, py):
                        tx, ty, px, py = nx, ny, tx, ty
                        break
                steps += 1
            distances[(x, y)].append(((tx, ty), steps, False))
            distances[(tx, ty)].append(((x, y), steps, True))
    return distances
