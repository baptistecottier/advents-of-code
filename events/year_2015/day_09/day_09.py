"""Advent of Code - Year 2015 - Day 09"""

from itertools import permutations, pairwise


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Process puzzle input and extract distances.

    Args:
        puzzle_input (str): Raw puzzle input containing distance information
        
    Returns:
        list[int]: List of extracted distances as integers
        
    Examples:
        >>> preprocessing("London to Dublin = 464")
        [464]
        >>> preprocessing("London to Dublin = 464\\nLondon to Belfast = 518")
        [464, 518]
    """
    distances = []
    for distance in puzzle_input.splitlines():
        distances.append(int(distance.split(' = ')[1]))
    return distances


def solver(routes: list[int]) -> tuple[int, int]:
    """
    Calculate shortest and longest distances between locations based on given routes.

    Args:
        routes (list[int]): List of distances between each pair of locations

    Returns:
        tuple[int, int]: (shortest possible distance, longest possible distance)
        
    Examples:
        >>> solver([464, 518, 141])  # London-Dublin, London-Belfast, Dublin-Belfast
        (605, 982)
        >>> solver([10, 15, 20])  # Three locations with simple distances
        (25, 35)
    """
    nb_locations = 1 + round((2 * len(routes)) ** 0.5)
    distances    = set()

    for route in permutations(range(nb_locations)):
        distance = 0
        for (a, b) in pairwise(route):
            n = min(a, b)
            delta = (a - n) + (b - n) - 1
            index = (n * (2 * nb_locations - n - 1)) // 2 + delta
            distance += routes[index]
        distances.add(distance)

    return (min(distances), max(distances))
