"""
Advent of Code - Year 2018 - Day 17
https://adventofcode.com/2018/day/17
"""

# Standard imports
import re


def preprocessing(puzzle_input: str):
    """
    Parse puzzle input to extract clay vein coordinates and return as a set of (x, y) positions.
    """
    clay = set()
    for vein in puzzle_input.splitlines():
        axis, start, end = map(int, re.findall(r'\d+', vein))
        if vein.startswith('x'):
            for y in range(start, end + 1):
                clay.add((axis, y))
        else:
            for x in range(start, end + 1):
                clay.add((x, axis))

    return clay


def solver(clay: list[tuple[int, int]]):
    """
    Simulates water flow
    """
    x, y = 500, 0
    y_min = min(y for _, y in clay)
    y_max = max(y for _, y in clay)
    rested = set()
    sources = [(500, 0)]
    while sources:
        x, y = source = sources.pop()

        # Find the bottom of a cave
        while (x, y + 1) not in clay and y <= y_max:
            y += 1
            rested.add((x, y))
        if y > y_max:
            continue

        rested.add((x, y))
        clay.add((x, y))

        # Fill up to the left side and find the left bound
        lx = x
        while (lx - 1, y) not in clay and (lx, y + 1) in clay:
            lx -= 1
            rested.add((lx, y))
            clay.add((lx, y))

        rx = x
        # Fill up to the right side and find the right bound
        while (rx + 1, y) not in clay and (rx, y + 1) in clay:
            rx += 1
            rested.add((rx, y))
            clay.add((rx, y))

        r_of = (rx, y + 1) not in clay
        l_of = (lx, y + 1) not in clay
        lx -= 1
        rx += 1

        while (r_of is False) and (l_of is False) and y > source[1]:
            y -= 1
            rested.add((x, y))
            clay.add((x, y))
            # Fill up to the left side
            tx = x
            while (tx - 1, y) not in clay:
                tx -= 1
                rested.add((tx, y))
                clay.add((tx, y))
                if (tx, y + 1) not in clay:
                    l_of = True
                    break
            lx = tx - 1

            # Fill up to the right side
            tx = x
            while (tx + 1, y) not in clay:
                tx += 1
                rested.add((tx, y))
                clay.add((tx, y))
                if (tx, y + 1) not in clay:
                    r_of = True
                    break
            rx = tx + 1

        # Update sources
        if r_of is True or l_of is True:
            clay.difference_update((tx, y) for tx in range(lx + 1, rx))
            new = [
                (tx, y)
                for tx, of in ((lx + 1, l_of), (rx - 1, r_of))
                if of and (tx, y + 1) not in rested
                ]
            if new:
                sources += [source] + new
    yield sum(y_min <= y <= y_max for _, y in rested)
    yield len(rested & clay)
