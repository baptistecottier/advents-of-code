"""Advent of Code - Year 2017 - Day 12"""

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
        left = communication.split(' <-> ')[1]
        communications.append(list(map(int,left.split(', '))))
    return communications


def solver(communications: list[list[int]]):
    """
    Identifies connected groups in a communication network and yields results.
    
    This function solves two problems:
    1. First yield: Returns the size of group containing program 0
    2. Second yield: Returns the total number of discrete groups in the network
    
    Args:
        communications (list[list[int]]): A list where each index i contains a list of programs
                                         that can communicate with program i
    
    Yields:
        int: First, the size of the group containing program 0
        int: Then, the total number of groups in the network
    
    Algorithm:
        Iteratively processes each unprocessed program, identifying all connected programs
        using a breadth-first search approach to find complete communication groups.
    """
    n_groups = 0
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
        if n_groups == 0:
            yield len(group)
        n_groups += 1

    yield n_groups
