"""
Advent of Code - Year 2019 - Day 20
https://adventofcode.com/2019/day/20
"""

from collections import defaultdict, deque


def preprocessing(puzzle_input: str) -> tuple[
        list[str],
        tuple[int, int],
        tuple[int, int],
        dict[tuple[int, int], tuple[int, int]]]:
    """
    Parses the puzzle input into a grid, start and end positions, and a mapping of portal gates.
    """
    grid = puzzle_input.splitlines()
    holes = defaultdict(set)
    h = len(grid)
    w = len(grid[0])
    for y, line in enumerate(grid[:-1]):
        for x, c in enumerate(line[:-1]):
            if c.isupper():
                if grid[y + 1][x].isupper():
                    gate_name = f"{line[x]}{grid[y + 1][x]}"
                    if y < h - 2 and grid[y + 2][x] == '.':
                        holes[gate_name].add((x - 2, y))
                    else:
                        holes[gate_name].add((x - 2, y - 3))

                elif grid[y][x + 1].isupper():
                    gate_name = line[x:x + 2]
                    if x < w - 2 and grid[y][x + 2] == '.':
                        holes[gate_name].add((x, y - 2))
                    else:
                        holes[gate_name].add((x - 3, y - 2))

    gates = {}
    for v in holes.values():
        if len(v) == 2:
            v = list(v)
            gates[v[0]] = v[1]
            gates[v[1]] = v[0]
    grid = [g[2:-2] for g in grid[2:-2]]
    start = holes['AA'].pop()
    end = holes['ZZ'].pop()
    return grid, start, end, gates


def solver(
        grid: list[str],
        start: tuple[int, int],
        end: tuple[int, int],
        gates: dict[tuple[int, int], tuple[int, int]]):
    """
    Finds the shortest path length(s) from a start to an end position in a grid with portals and
    recursive levels, yielding results as they are found.
    """
    h, w = len(grid), len(grid[0])
    queue = deque([[(*start, 0)]])
    seen = set([(*start, 0)])
    length_with_portals = -1

    while queue:
        path = queue.popleft()
        x, y, level = path[-1]

        if (x, y) == end:
            if length_with_portals == -1:
                length_with_portals = len(path) - 1
            if level == 0 and length_with_portals != -1:
                return length_with_portals, len(path) - 1
        else:
            for tx, ty in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (
                        (tx, ty, level) not in seen and
                        0 <= tx < w and
                        0 <= ty < h and
                        grid[ty][tx] == '.'):
                    queue.append(path + [(tx, ty, level)])
                    seen.add((tx, ty, level))
            if (x, y) in gates:
                if x in [0, w - 1] or y in [0, h - 1]:
                    level -= 1
                else:
                    level += 1
                tx, ty = gates[(x, y)]
                if (tx, ty, level) not in seen and level >= 0:
                    queue.append(path + [(tx, ty, level)])
                    seen.add((tx, ty, level))
    raise ValueError("No path found!")
