"""
Advent of Code - Year 2022 - Day 24
https://adventofcode.com/2022/day/24
"""

from collections import deque, defaultdict
import math


def extract_map(lines):
    """
    Extracts walls and blizzard positions from input lines, computing blizzard locations for all
    time steps. Returns a set of wall coordinates and a dictionary mapping time to sets of blizzard
    positions.
    """
    walls = set()
    blizzards = []
    w = len(lines[0]) - 2
    h = len(lines) - 2

    for y, line in enumerate(lines, -1):
        for x, c in enumerate(line, -1):
            match c:
                case '#': walls.add((x, y))
                case '>': blizzards.append((x, y, 1, 0))
                case 'v': blizzards.append((x, y, 0, 1))
                case '<': blizzards.append((x, y, -1, 0))
                case '^': blizzards.append((x, y, 0, -1))
                case _:
                    continue

    blizzard_by_minute = defaultdict(set)

    for t in range(math.lcm(w, h)):
        for bx, by, dx, dy in blizzards:
            blizzard_by_minute[t].add((
                (bx + dx * t) % w,
                (by + dy * t) % h))

    return walls, blizzard_by_minute


def preprocessing(puzzle_input):
    """
    Parses puzzle input to extract walls, blizzard positions at each time step, start/end points,
    and grid dimensions. Returns preprocessed data structures for pathfinding through a
    blizzard-filled valley.
    """
    lines = puzzle_input.splitlines()

    walls, blizzards_by_minute = extract_map(lines)

    h = len(lines) - 2
    x_start = lines[0].index('.') - 1
    walls.add((x_start, -2))

    x_end = lines[-1].index('.') - 1
    walls.add((x_end, h + 1))

    return walls, blizzards_by_minute, (x_start, -1), (x_end, h)


def solver(walls, blizzard_by_minute, start, target):
    """
    Solves the blizzard crossing puzzle by finding the shortest path from start to target,
    then back to start, and finally back to target again.
    """

    time_1 = cross_blizzard(walls, blizzard_by_minute, start, target, 0)
    yield time_1
    time_2 = cross_blizzard(walls, blizzard_by_minute, target, start, time_1)
    time_3 = cross_blizzard(walls, blizzard_by_minute, start, target, time_2)
    yield time_3


def cross_blizzard(walls, blizzard_by_minute, start, target, minutes):
    """
    Find the shortest path from start to target while avoiding moving blizzards using BFS.
    Returns the minimum time needed to reach the target position.
    """

    queue = deque([(*start, minutes)])
    visited = set()
    cycle_length = len(blizzard_by_minute)

    while queue:
        x, y, time = queue.popleft()

        if (x, y) == target:
            return time

        state = (x, y, time % cycle_length)
        if state in visited:
            continue
        visited.add(state)

        for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            pos = x + dx, y + dy

            if pos in walls:
                continue

            if pos in blizzard_by_minute[(time + 1) % cycle_length]:
                continue

            queue.append((*pos, time + 1))
    raise ValueError("Too much blizzard! Target unreachable!")
