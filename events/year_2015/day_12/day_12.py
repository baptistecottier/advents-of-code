"""
Advent of Code - Year 2015 - Day 12
https://adventofcode.com/2015/day/12
"""

from json import loads


def solver(document: str) -> tuple[int, int]:
    """
    Calculate sums based on JSON document parsing with different filtering options.

    Args:
        document (str): JSON formatted string to process

    Returns:
        tuple[int, int]: Two sum values - first with red values included, second excluding red
                         values

    Examples:
        >>> solver('[1,2,3]')
        (6, 6)
        >>> solver('{"a":2,"b":4}')
        (6, 6)
        >>> solver('{"a":2,"b":"red","c":4}')
        (6, 0)
        >>> solver('[1,{"c":"red","b":2},3]')
        (6, 4)
    """
    return (
        get_sum(loads(document), allow_red=True),
        get_sum(loads(document), allow_red=False),
    )


def get_sum(document: int | list | dict, allow_red: bool) -> int:
    """
    Calculate sum of all numbers in a nested document structure.

    This function recursively processes a document that can contain integers, lists, and
    dictionaries, summing all integer values encountered while respecting special rules for
    dictionaries containing 'red'.

    Args:
        document (int | list | dict): The input document to process. Can be:
            - An integer value
            - A list containing any combination of integers, lists, or dictionaries
            - A dictionary with any values
        allow_red (bool): Flag to control handling of dictionaries containing 'red':
            - If True: Include values from dictionaries containing 'red'
            - If False: Skip dictionaries containing 'red' (return 0)

    Returns:
        int: Sum of all integer values found in the document structure,
             excluding values from dictionaries containing 'red' when allow_red is False

    Example:
        >>> get_sum({"a": 2, "b": 4}, True)
        6
        >>> get_sum({"a": 2, "b": "red", "c": 4}, False)
        0
        >>> get_sum([1, {"c": "red", "b": 2}, 3], False)
        4
    """
    if isinstance(document, int):
        return document
    if isinstance(document, list):
        return sum(get_sum(subdocument, allow_red) for subdocument in document)
    if isinstance(document, dict):
        if allow_red or "red" not in document.values():
            return get_sum(list(document.values()), allow_red)
    return 0
