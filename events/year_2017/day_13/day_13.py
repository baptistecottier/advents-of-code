"""Advent of Code - Year 2017 - Day 13"""

from collections.abc import Generator
from dataclasses import dataclass

@dataclass
class Scan:
    """Class storing scan parameters"""
    depth: int
    range: int

    @property
    def duration(self):
        """Return the duration of a scan"""
        return 2 * (self.range - 1)


def preprocessing(puzzle_input: str) -> list[Scan]:
    """
    Stores depth, range for each scan given records in the puzzle input
    
    Args:
        puzzle_input (str): raw string from input file
            Example:
                0: 3
                1: 2
                4: 4
                6: 4

    Returns:
        list[Scan]: list of Scan objects
            Example:
                [Scan(depth=0, range=3),
                 Scan(depth=1, range=2),
                 Scan(depth=4, range=4),
                 Scan(depth=6, range=4)]
    """
    scans = []
    for line in puzzle_input.splitlines():
        scan_depth, scan_range = ([int(item) for item in line.split(': ')])
        scans.append(Scan(scan_depth, scan_range))
    return scans


def solver(scans: list[Scan]) -> Generator[int, None, None]:
    """
    Solves the firewall traversal problem.
    
    Part 1: Calculates the severity of being caught while traversing a firewall without delay.
    Part 2: Finds the minimum delay required to traverse the firewall without being caught.
    
    Args:
        scans: List of Scan objects representing the firewall layers.
    
    Yields:
        int: First, the total severity if starting with no delay.
                Second, the minimum delay required to pass through without being caught.
    """
    severity = 0
    for scan in scans:
        if scan.depth % scan.duration == 0:
            severity += scan.depth * scan.range
    yield severity

    delay = 1
    while any((scan.depth + delay) % scan.duration == 0 for scan in scans):
        delay += 1
    yield delay
