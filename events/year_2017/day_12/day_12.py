"""
Advent of Code - Year 2017 - Day 12
https://adventofcode.com/2017/day/12
"""


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Returns a list of lists containing pipe connections between programs.

    Example
        >>> preprocessing(0 <-> 1, 2\n1 <-> 1\n2 <-> 0)
        [[1, 2], [1], [0]]

    Note
        Left part of the connection is implicited stored as the list index
    """
    communications = []
    for communication in puzzle_input.splitlines():
        left = communication.split(" <-> ")[1]
        communications.append(list(map(int, left.split(", "))))
    return communications


def solver(communications: list[list[int]]) -> tuple[int, int]:
    """
    Find connected components in a communication network graph.

    Args:
        communications: List where communications[i] contains nodes connected to node i

    Returns:
        tuple: (size of first group found, total number of groups)

    Examples:
        >>> solver([[1, 2], [0], [0, 3, 4], [2], [2]])
        (3, 2)
        >>> solver([[1], [0, 2], [1]])
        (3, 1)
    """
    groups = []
    size = len(communications)
    to_group = set(range(size))

    while to_group:
        i = to_group.pop()
        group = set()
        pipes = set(communications[i])

        while not pipes.issubset(group):
            group.update(pipes)
            for item in pipes.copy():
                pipes.update(communications[item])
        to_group.difference_update(group)
        groups.append(len(group))

    return groups[0], len(groups)
