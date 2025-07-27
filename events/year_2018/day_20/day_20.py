"""
Advent of Code - Year 2018 - Day 20
https://adventofcode.com/2018/day/20
"""

import networkx


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Parses a regex-like path string to build a maze graph and returns shortest path lengths from
    origin.
    """
    maze = networkx.Graph()
    paths = puzzle_input[1:-1]

    pos = {0}
    branch = []
    starts = {0}
    ends = set()

    for c in paths:
        match c:
            case 'N':
                maze.add_edges_from((p, p + 1) for p in pos)
                pos = {p + 1 for p in pos}
            case 'E':
                maze.add_edges_from((p, p + 1j) for p in pos)
                pos = {p + 1j for p in pos}
            case 'S':
                maze.add_edges_from((p, p - 1) for p in pos)
                pos = {p - 1 for p in pos}
            case 'W':
                maze.add_edges_from((p, p - 1j) for p in pos)
                pos = {p - 1j for p in pos}
            case '(':
                branch.append((starts, ends))
                starts, ends = pos, set()
            case '|':
                ends.update(pos)
                pos = starts
            case ')':
                pos.update(ends)
                starts, ends = branch.pop()

    return networkx.algorithms.shortest_path_length(maze, source=0).values()


def solver(lengths: list[int]) -> tuple[int, int]:
    """
    Solves the puzzle by finding the maximum path length and counting paths with length >= 1000.
    """
    return max(lengths), sum(length >= 1000 for length in lengths)
