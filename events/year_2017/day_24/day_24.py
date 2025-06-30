"""Advent of Code - Year 2017 - Day 24"""

from copy import deepcopy
from pythonfw.functions import extract_chunks

def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Extract and convert chunks of input data into a list of 2-element lists of integers.
    """
    return extract_chunks(puzzle_input, 2)


def solver(connections: list[list[int]]):
    """
    Solve bridge building puzzle by finding the strongest and longest bridges.
    
    Args:
        connections: List of port connections, each represented as a list of two integers.
        
    Yields:
        int: First, the strength of the strongest bridge.
        int: Second, the strength of the longest (and if tied, strongest) bridge.
    """
    bridges = build_bridges(connections, 0, [(0,0)])
    yield max(bridges, key = lambda x: x[1])[1]
    yield max(bridges)[1]


def build_bridges(components: list[list[int]], port: int, strength: list[tuple[int, int]]):
    """
    Recursively builds all possible bridges from the given components, starting with a specific 
    port. Each bridge is evaluated based on its length and total strength. The function explores all
    possible combinations by connecting compatible components.
    Args:
        components: List of components, where each component is a list of two integers
                    representing ports.
        port: The current port value to connect to.
        strength: List containing a single tuple of (length, total_strength) for the current bridge.
    Returns:
        List of tuples, where each tuple contains (length, total_strength) for a complete bridge.
    """
    candidates = [c for c in components if port in c]
    if not candidates:
        return strength

    for c in candidates:
        cc = deepcopy(components)
        cc.remove(c)
        strength += build_bridges(
            cc,
            sum(c) - port,
            [(strength[0][0] + 1, strength[0][1] + sum(c))])

    return strength
