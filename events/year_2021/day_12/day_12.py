"""
Advent of Code - Year 2021 - Day 12
https://adventofcode.com/2021/day/12
"""


def preprocessing(puzzle_input: str) -> dict[str, list[str]]:
    """
    Parses the puzzle input into a dictionary representing bidirectional paths between nodes,
    excluding connections to 'start' as a destination.
    """
    paths = {}
    for path in puzzle_input.splitlines():
        start, end = path.split('-')
        if end != 'start':
            if start in paths:
                paths[start].append(end)
            else:
                paths[start] = [end]
        if start != 'start':
            if end in paths:
                paths[end].append(start)
            else:
                paths[end] = [start]
    return paths


def solver(caves: dict[str, list[str]]) -> tuple[int, int]:
    """
    Solves the cave pathfinding problem by returning the number of paths visiting small caves once
    and the total with one small cave visited twice.
    """
    once, twice = get_all_paths(caves).values()
    return once, once + twice


def get_all_paths(caves, pos='start', path=None, paths_count=None, twice=True
                  ) -> dict[bool, int]:
    """
    Recursively counts all possible paths from 'start' to 'end' in a cave system, allowing one
    small cave to be visited twice if specified.
    """
    if path is None:
        path = []
    if paths_count is None:
        paths_count = {True: 0, False: 0}

    if pos == 'end':
        paths_count[twice] += 1
        return paths_count
    for dst in caves[pos]:
        if dst.isupper():
            get_all_paths(caves, dst, path + [dst], paths_count, twice)
        elif dst.islower() and path.count(dst) <= twice:
            get_all_paths(caves, dst, path + [dst], paths_count, path.count(dst) < twice)
    return paths_count
