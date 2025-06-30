"""Advent of Code - Year 2015 - Day 16"""

from operator import eq, lt, gt
from collections.abc import Callable
from copy     import deepcopy
from parse    import parse, Result


def preprocessing(puzzle_input: str):
    """
    Preprocesses puzzle input to extract information about aunts and their possessions.

    This function takes a string input containing information about multiple aunts and their
    possessions, parses it, and converts it into a list of dictionaries where each dictionary
    represents an aunt's possessions.

    Args:
        puzzle_input (str): A string containing multiple lines of aunt data in the format
                           'Sue N: item1: count1, item2: count2, item3: count3'

    Returns:
        list[dict]: A list of dictionaries where each dictionary contains three key-value pairs
                    representing an aunt's possessions. The keys are the item names (strings)
                    and the values are the corresponding counts (integers).

    Example:
        >>> input_str = "Sue 1: cars: 9, akitas: 3, goldfish: 0"
        >>> preprocessing(input_str)
        [{'cars': 9, 'akitas': 3, 'goldfish': 0}]
    """
    aunts = []
    for aunt_data in puzzle_input.splitlines():
        result = parse("Sue {:d}: {}: {:d}, {}: {:d}, {}: {:d}", aunt_data)
        if isinstance(result, Result):
            _, c1, v1, c2, v2, c3, v3 = result
            aunts.append({c1: v1, c2: v2, c3: v3})
    return aunts


def solver(aunts: list):
    """
    Solves the Aunt Sue puzzle for both parts.

    Args:
        aunts: Dictionary containing information about all Aunt Sues.

    Yields:
        int: The ID of the Aunt Sue matching the criteria for part 1.
        int: The ID of the Aunt Sue matching the modified criteria for part 2.
    """
    yield find_sue(deepcopy(aunts), eq, eq)
    yield find_sue(aunts, gt, lt)


def find_sue(aunts: list, op1: Callable, op2: Callable):
    """
    Identifies the aunt Sue based on compound values and comparison operations.

    Args:
        aunts (list): List of dictionaries where each dictionary represents an aunt's compounds and
                      their values.
        op1 (function): Comparison operator for 'cats' and 'trees'.
        op2 (function): Comparison operator for 'pomeranians' and 'goldfish'.

    Returns:
        int or None: The number of the aunt Sue that matches the criteria, or None if no match is
                     found.
    """
    sue = { "children": 3, "cats":     7, "samoyeds": 2, "pomeranians":  3, "akitas":   0,
            "vizslas":  0, "goldfish": 5, "trees":    3, "cars":         2, "perfumes": 1}
    for n, compounds in enumerate(aunts, 1):
        for compound, value in list(compounds.items()):
            if compound in ['cats', 'trees']:
                if op1(value, sue[compound]):
                    del compounds[compound]
                else: break
            elif compound in ['pomeranians', 'goldfish']:
                if op2(value, sue[compound]):
                    del compounds[compound]
                else: break
            elif value == sue[compound]:
                del compounds[compound]
        if compounds == {}:
            return n
    return None
