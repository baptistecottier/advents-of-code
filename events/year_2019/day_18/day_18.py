"""
Advent of Code - Year 2019 - Day 18
https://adventofcode.com/2019/day/18
"""

from collections import defaultdict, deque
from collections.abc import Iterator
import heapq


def preprocessing(puzzle_input: str) -> tuple[list[list[str]], tuple[int, int], int]:
    """
    Parses the puzzle input into a grid, the entrance coordinates, and the number of keys present.
    """
    entrance = (-1, -1)
    grid = []
    n_keys = len([c for c in puzzle_input if c.islower()])
    for y, line in enumerate(puzzle_input.splitlines()):
        if '@' in line:
            entrance = (line.index('@'), y)
        grid.append(list(line))
    return grid, entrance, n_keys


def solver(grid: list[list[str]], entrance: tuple[int, int], n_keys: int) -> Iterator[int]:
    """
    Solves the shortest path to collect all keys in a grid-based puzzle, starting from the entrance,
    using BFS.
    """
    yield fewest_steps(grid, (entrance,), n_keys)

    x, y = entrance
    names = "@&%$"
    entrances: tuple[tuple[int, int], ...] = ()
    for i, (dx, dy) in enumerate(((1, 1), (1, -1), (-1, 1), (-1, -1))):
        grid[y + dy][x + dx] = names[i]
        entrances += ((x + dx, y + dy),)
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        grid[y + dy][x + dx] = '#'
    grid[y][x] = '#'
    yield fewest_steps(grid, entrances, n_keys)


def fewest_steps(grid: list[list[str]], entrances: tuple[tuple[int, int], ...], n_keys: int) -> int:
    """
    Returns the fewest steps needed by the robots, starting from the entrances, to collect all the
    keys. Explores the (robot positions, keys) states with Dijkstra, moving one robot at a time to a
    neighbouring key whose doors are open.
    """
    distances = keys_distances(grid, entrances)
    robots = "".join(grid[y][x] for x, y in entrances)
    queue = [(0, robots, frozenset())]
    positions = defaultdict(lambda: 100_000)

    while queue:
        steps, robots, keys = heapq.heappop(queue)
        if len(keys) == n_keys:
            return steps
        for i, robot in enumerate(robots):
            for k, d, s in distances[robot]:
                if d <= keys:
                    new_robots = robots[:i] + k + robots[i + 1:]
                    if positions[(new_robots, keys | {k})] <= steps + s:
                        continue
                    positions[(new_robots, frozenset(keys | {k}))] = steps + s
                    heapq.heappush(queue, (steps + s, new_robots, keys | {k}))
    raise ValueError("Impossible to collect all the keys")


def keys_distances(
        grid: list[list[str]],
        entrances: tuple[tuple[int, int], ...]) -> dict[str, list[tuple[str, frozenset[str], int]]]:
    """
    Maps each entrance and each key to the neighbouring keys, reachable without passing another
    key, with the doors on the way and the distance, using BFS.
    """
    distances = {}
    starting_points = deque([*entrances])  # Starting points
    started = set()
    while starting_points:
        x, y = starting_points.pop()
        started.add(grid[y][x])
        queue = deque([(x, y, frozenset(), 0)])
        start = grid[y][x]
        distances[start] = []
        visited = {(x, y)}
        while queue:
            x, y, doors, dist = queue.popleft()
            for (tx, ty) in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
                if (tx, ty) in visited or grid[ty][tx] == '#':
                    continue
                if not (0 <= tx < len(grid[0]) and 0 <= ty < len(grid)):
                    continue
                visited.add((tx, ty))
                if grid[ty][tx].islower():
                    distances[start].append((grid[ty][tx], doors, dist + 1))
                    if grid[ty][tx] not in started:
                        starting_points.append((tx, ty))
                        started.add(grid[ty][tx])
                else:
                    if grid[ty][tx].isupper():
                        queue.append((tx, ty, doors | {grid[ty][tx].lower()}, dist + 1))
                    queue.append((tx, ty, doors, dist + 1))
    return distances
