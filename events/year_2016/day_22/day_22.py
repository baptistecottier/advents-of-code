"""
Advent of Code - Year 2016 - Day 22
https://adventofcode.com/2016/day/22
"""

# Standard imports
from dataclasses import dataclass
from itertools import product

# First-class imports
from pythonfw.functions import extract_chunks
from pythonfw.classes import Point


@dataclass
class Node:
    """
    A class representing a node in a grid storage system.
    This class represents a storage node with its position coordinates and storage metrics.
    Attributes:
        x (int): The x-coordinate position of the node in the grid.
        y (int): The y-coordinate position of the node in the grid.
        size (int): The total storage capacity of the node.
        used (int): The amount of storage currently in use.
        avail (int): The amount of available storage remaining.
    Properties:
        pt: Returns a Point object representing the node's (x,y) coordinates.
    """

    x: int
    y: int
    size: int
    used: int
    avail: int

    @property
    def pt(self):
        """
        Returns a Point object representation of the current coordinates.

        Returns:
            Point: A Point object with the current x and y coordinates.
        """
        return Point(self.x, self.y)


def preprocessing(puzzle_input: str) -> list[Node]:
    """
    Parse puzzle input and create a list of Node objects.

    Args:
        puzzle_input: Raw puzzle input string containing node data

    Returns:
        List of Node objects created from extracted parameters

    Example:
        >>> preprocessing("node1 data\nnode2 data\n")
        [Node(...), Node(...)]
    """
    nodes = []
    for param in extract_chunks(puzzle_input, take=5, skip=1):
        nodes.append(Node(*param))
    return nodes


def solver(nodes: list[Node]) -> tuple[int, int]:
    """
    Solves the puzzle by analyzing node usage and movement.

    Args:
        nodes (list[Node]): List of Node objects representing the grid.

    Yields:
        int: Number of viable node pairs.
        int: Minimum number of steps to move data to the target.
    """
    empty = None
    walls = set()
    n_viable_node_pairs = sum(na.used < nb.avail for (na, nb) in product(nodes, nodes) if na.used)

    for node in nodes:
        if node.used == 0:
            empty = node.pt
        if node.used > 100:
            walls.add(node.pt)
    pt_min = min(walls, key=lambda x: x.manhattan())
    if pt_min.x != 0:
        wall = pt_min
        wall.move(-1, 0)
    else:
        wall = max(walls, key=lambda x: x.manhattan())
        wall.move(1, 0)
    width = max(node.x for node in nodes)
    if empty is not None:
        return (n_viable_node_pairs,
                empty.manhattan(wall.x, wall.y) +
                wall.manhattan(width, 0) + 5 * (width - 1)
                )
    raise ValueError("No way to move data to the target")
