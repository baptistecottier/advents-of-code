"""Advent of Code - Year 2015 - Day 03"""


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


def solver(directions: list[tuple[int, int]]):
    "Simulate deliveries, for Santa only first then with the help of Robo-Santa"
    yield deliver(directions.copy(), 1)
    yield deliver(directions[:-1], 2)


def deliver(directions: list[tuple[int, int]], n: int) -> int | None:
    """
    Calculate the number of houses receiving at least one present.

    Santa and his helpers deliver presents by following directions, with each deliverer taking
    turns moving according to the provided directions. Multiple deliverers can visit the same house.

    Args:
        directions (list[tuple[int, int]]): List of movement directions, where each tuple contains
            (dx, dy) representing movement in x and y directions respectively.
        n (int): Number of deliverers (e.g., 1 for just Santa, 2 for Santa and Robo-Santa)

    Returns:
        int: Number of unique houses that received at least one present

    Example:
        >>> directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        >>> deliver(directions, 2)
        4
    """

    deliverers = [(0, 0) for _ in range(n)]
    houses     = {(0, 0)}

    while directions:
        dx, dy = directions.pop(0)
        x, y = deliverers.pop(0)
        houses.add((dx + x, dy + y))
        deliverers.append((dx + x, dy + y))
    return len(houses)
