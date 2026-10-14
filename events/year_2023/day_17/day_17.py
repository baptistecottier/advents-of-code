"""
Advent of Code - Year 2023 - Day 17
https://adventofcode.com/2023/day/17
"""

import heapq


def preprocessing(puzzle_input):
    """
    Parse input into a 2D grid of integers.
    """
    return [[int(item) for item in line] for line in puzzle_input.splitlines()]


def solver(grid):
    """
    Solves the heat loss puzzle for both part 1 and part 2.
    Yields minimum heat loss for standard (1-3 steps) and ultra (4-10 steps) crucibles.
    """
    yield find_lowest_heat(grid, 1, 3)
    yield find_lowest_heat(grid, 4, 10)


def find_lowest_heat(grid, min_blocks, max_blocks):
    """
    Find the minimum heat loss path using Dijkstra's algorithm with movement constraints.
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = [(0, 0, 0, 0, 1), (0, 0, 0, 1, 1)]
    visited = set()

    while pq:
        loss, x, y, direction, blocks = heapq.heappop(pq)

        if (x, y, direction, blocks) in visited:
            continue
        visited.add((x, y, direction, blocks))

        if x == y == len(grid) - 1 and blocks >= min_blocks:
            return loss

        for next_dir in [(direction - 1) % 4, direction, (direction + 1) % 4]:
            nx, ny = x + directions[next_dir][0], y + directions[next_dir][1]

            if 0 <= nx < len(grid) and 0 <= ny < len(grid):
                next_state = (nx, ny, next_dir, blocks + 1 if next_dir == direction else 1)

                if next_state in visited:
                    continue

                if ((next_dir == direction and blocks < max_blocks) or
                        (next_dir != direction and blocks >= min_blocks)):
                    heapq.heappush(pq, (loss + grid[ny][nx], *next_state))

    raise ValueError("No path found!?")
