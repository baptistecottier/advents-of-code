"""Advent of Code - Year 2015 - Day 16"""

# Standard imports
from collections.abc import Callable
from copy import deepcopy
from operator import eq, lt, gt

# Third-party import
from parse import parse, Result


def preprocessing(puzzle_input: str) -> list[dict]:
    """
    Parse puzzle input into a list of dictionaries representing aunts' properties.
    Each line in the input represents an aunt and is parsed to extract compound-value pairs.

    Parameters:
        puzzle_input (str): Multi-line string with aunt data

    Returns:
        list[dict]: List of dictionaries where each dict contains compound-value pairs for an aunt

    Example:
        >>> preprocessing("Sue 1: cars: 9, akitas: 3, goldfish: 0")
        [{'cars': 9, 'akitas': 3, 'goldfish': 0}]
    """
    aunts = []
    for aunt_data in puzzle_input.splitlines():
        result = parse("Sue {:d}: {}: {:d}, {}: {:d}, {}: {:d}", aunt_data)
        if isinstance(result, Result):
            _, c1, v1, c2, v2, c3, v3 = result
            aunts.append({c1: v1, c2: v2, c3: v3})
    return aunts


def solver(aunts: list) -> tuple[int, int]:
    """
    Finds the correct Aunt Sue using different comparison methods.

    Args:
        aunts: List of aunts with their known properties.

    Returns:
        Tuple containing:
            - The Sue number found using equality comparison for all properties
            - The Sue number found using custom comparison (gt for some, lt for others)

    Example:
        >>> solver([{'number': 1, 'cats': 7}, {'number': 2, 'trees': 3}])
        (1, 2)
    """
    return (find_sue(deepcopy(aunts), eq, eq), find_sue(aunts, gt, lt))


def find_sue(aunts: list, op1: Callable, op2: Callable) -> int:
    """
    Find the aunt Sue that matches the MFCSAM reading based on compound comparisons.

    Uses different comparison operators for specific compounds:
    - op1 for 'cats' and 'trees'
    - op2 for 'pomeranians' and 'goldfish'
    - equality check for all other compounds

    Args:
        aunts: List of dictionaries, each representing an aunt with her compounds
        op1: Comparison operator for 'cats' and 'trees'
        op2: Comparison operator for 'pomeranians' and 'goldfish'

    Returns:
        The number of the matching aunt or -1 if not found

    Example:
        >>> aunts = [{'cats': 8}, {'goldfish': 3}, {'cars': 2, 'perfumes': 1}]
        >>> find_sue(aunts, operator.gt, operator.lt)
        3
    """
    sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    for n, compounds in enumerate(aunts, 1):
        for compound, value in list(compounds.items()):
            if compound in ["cats", "trees"]:
                if op1(value, sue[compound]):
                    del compounds[compound]
                else:
                    break
            elif compound in ["pomeranians", "goldfish"]:
                if op2(value, sue[compound]):
                    del compounds[compound]
                else:
                    break
            elif value == sue[compound]:
                del compounds[compound]
        if compounds == {}:
            return n
    return -1
