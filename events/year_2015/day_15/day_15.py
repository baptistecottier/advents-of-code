"""
Advent of Code - Year 2015 - Day 15
https://adventofcode.com/2015/day/15
"""

# Standard imports
from collections import defaultdict
from math import prod

# First-party import
from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Extract ingredient properties from puzzle input into chunks of 5 values.

    Args:
        puzzle_input: Raw puzzle input string
    Returns:
        List of lists, each containing 5 numeric values per ingredient
    """
    return extract_chunks(puzzle_input, 5)


def solver(ingredients: list[list[int]]) -> tuple[int, int]:
    """
    Find the highest score cookie recipe that can be made with the given ingredients.

    Args:
        ingredients: List of ingredient properties (capacity, durability, flavor, texture, calories)

    Returns:
        Tuple of (highest possible score, highest score with exactly 500 calories)

    Example:
        >>> ingredients = [[2, 0, -2, 0, 3], [0, 5, -3, 0, 3], [0, 0, 5, -1, 8], [0, -1, 0, 5, 8]]
        >>> solver(ingredients)
        (62842880, 57600000)

        >>> ingredients = [[5, -1, 0, 0, 5], [-1, 3, 0, 0, 1]]
        >>> solver(ingredients)
        (62842880, 57600000)
    """
    scores = defaultdict(list)

    for frosting in range(101):
        for candy in range(101 - frosting):
            for butterscotch in range(101 - (frosting + candy)):
                sugar = 100 - (frosting + candy + butterscotch)
                properties = compute_properties([frosting, candy, butterscotch, sugar], ingredients)
                scores[properties[4]].append(prod(properties[:4]))

    return (max(sum(scores.values(), [])), max([0, *scores[500]]))


def compute_properties(
    proportions: list[int], ingredients: list[list[int]]
) -> list[int]:
    """
    Calculate the properties of a cookie based on ingredient proportions.

    Args:
        proportions: List of amounts for each ingredient
        ingredients: List of ingredient properties

    Returns:
        List of computed property values after applying proportions

    Example:
        >>> ingredients = [[2, 0, -2, 0, 3], [0, 5, -3, 0, 3], [0, 0, 5, -1, 8], [0, -1, 0, 5, 8]]
        >>> compute_properties([44, 56, 0, 0], ingredients)
        [44, 280, -92, 0, 168]
        >>> compute_properties([40, 60, 0, 0], ingredients)
        [40, 300, -120, 0, 180]
    """
    return [
        max(0, sum(a * b[i] for a, b in zip(proportions, ingredients)))
        for i in range(5)
    ]
