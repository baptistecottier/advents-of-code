"""
Advent of Code - Year 2024 - Day 16
https://adventofcode.com/2024/day/16
"""

# Standard imports
from collections import deque, defaultdict

# First party imports
from pythonfw.classes import Particule2D


def preprocessing(puzzle_input: str
                  ) -> tuple[set[tuple[int, int]], tuple[int, int], tuple[int, int]]:
    """
    Parses the puzzle input to extract kiosk positions, start, and end coordinates.
    """
    kiosk = set()
    start = (-1, -1)
    end = (-1, -1)

    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            match c:
                case '#': kiosk.add((x, y))
                case 'S': start = (x, y)
                case 'E': end = (x, y)
                case _: pass

    return kiosk, start, end


def solver(kiosk: set[tuple[int, int]], start: tuple[int, int], end: tuple[int, int]
           ) -> tuple[int, int]:
    """
    Finds the lowest score and the number of unique tiles in the best path from start to end,
    avoiding kiosk positions.
    """
    paths = deque([[(Particule2D(start, (1, 0)), 0,)]])
    scores = defaultdict(lambda: 1_000_000)
    best_paths_tiles = set()
    lowest_score = 1_000_000

    while paths:
        path = paths.popleft()
        pt, path_score = path[-1]

        if pt.xy() == end:
            if path_score == lowest_score:
                best_paths_tiles.update(pt.xy() for (pt, _) in path)
            elif path_score < lowest_score:
                best_paths_tiles = set(pt.xy() for (pt, _) in path)
                lowest_score = path_score
        else:
            for vx, vy in ((pt.vel.x, pt.vel.y),
                           (-pt.vel.y, pt.vel.x),
                           (pt.vel.y, -pt.vel.x)):
                pos_score = scores[(pt.pos.x + vx, pt.pos.y + vy)]

                if path_score < pos_score + 1_000 and (pt.pos.x + vx, pt.pos.y + vy) not in kiosk:
                    delta = 1 if vx == pt.vel.x else 1_001
                    paths.append(path + [(Particule2D((pt.pos.x + vx, pt.pos.y + vy), (vx, vy)),
                                          path_score + delta)])
                    scores[(pt.pos.x + vx, pt.pos.y + vy)] = min(pos_score, path_score + delta)

    return lowest_score, len(best_paths_tiles)
