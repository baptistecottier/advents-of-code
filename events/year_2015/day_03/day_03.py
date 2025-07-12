"""Advent of Code - Year 2015 - Day 03"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[tuple[int, int]]:
    """
    Convert a string of direction symbols into a list of coordinate tuples.

    Parameters:
        puzzle_input (str): A string containing only the characters '^', '>', 'v', '<' representing
        directions.

    Returns:
        list[tuple[int, int]]: A list of tuples where each tuple contains (x, y) coordinates:
            '^' -> (0, 1)   [North]
            '>' -> (1, 0)   [East]
            'v' -> (0, -1)  [South]
            '<' -> (-1, 0)  [West]

    Raises:
        KeyError: If the input string contains any characters other than '^', '>', 'v', '<'

    Example:
        >>> preprocessing('^>v<')
        [(0, 1), (1, 0), (0, -1), (-1, 0)]
    """
    converter  = {'^': (0,  1), '>': (1 , 0), 'v': (0, -1), '<': (-1, 0)}
    directions = []
    for direction in puzzle_input:
        if direction not in "<>^v":
            raise KeyError((f"Wrong input: {direction}."
                            "Should be any of '<', '>', '^', and 'v'"))
        directions.append(converter[direction])
    return directions


def solver(directions: list[tuple[int, int]]) -> Iterator[int]:
    """
    Simulate deliveries, for Santa only first then with the help of Robo-Santa
    """
    yield deliver(directions.copy(), 1)
    yield deliver(directions[:-1], 2)


def deliver(directions: list[tuple[int, int]], n: int) -> int:
    """
    Simulates n deliverers moving according to given directions and delivering presents to houses.
    
    Args:
        directions: List of (dx, dy) tuples representing movement directions.
        n: Number of deliverers.
    
    Returns:
        Number of unique houses that received at least one present.
        
    Examples:
        >>> deliver([(0, 1), (0, 1)], 1)  # Single deliverer going north twice
        3
        >>> deliver([(0, 1), (1, 0)], 2)  # Two deliverers, one goes north, one goes east
        3
    """
    deliverers = [(0, 0) for _ in range(n)]
    houses     = {(0, 0)}

    while directions:
        dx, dy = directions.pop(0)
        x, y = deliverers.pop(0)
        houses.add((dx + x, dy + y))
        deliverers.append((dx + x, dy + y))
    return len(houses)
