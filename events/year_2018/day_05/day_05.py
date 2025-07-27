"""
Advent of Code - Year 2018 - Day 5
https://adventofcode.com/2018/day/5
"""

import string


def solver(polymer: str) -> tuple[int, int]:
    """
    Solve polymer reduction puzzle by removing reactive units and finding shortest possible polymer.

    Args:
        polymer (str): Input polymer string containing uppercase and lowercase letters.

    Returns:
        tuple[int, int]: (length after full reduction,
                          shortest possible length after removing one unit type)

    Examples:
        >>> solver("dabAcCaCBAcCcaDA")
        (10, 4)
        >>> solver("aA")
        (0, 0)
    """
    units = list(zip(string.ascii_lowercase, string.ascii_uppercase))
    new_length = 0
    shortest_polymer = len(polymer)

    for unit_low, unit_up in units + [('', '')]:
        new_polymer = polymer.replace(unit_low, '').replace(unit_up, '')

        length = len(new_polymer)
        while length != new_length:
            length = len(new_polymer)
            for low, up in units:
                new_polymer = new_polymer.replace(low + up, '').replace(up + low, '')
            new_length = len(new_polymer)
        shortest_polymer = min(shortest_polymer, new_length)

    return new_length, shortest_polymer
