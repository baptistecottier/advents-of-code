"""Advent of Code - Year 2015 - Day 08"""

from ast import literal_eval


def solver(strings: str):
    """
    Calculates the difference between encoded and decoded string lengths.

    Args:
        strings (str): A multi-line string containing escaped sequences.

    Returns:
        tuple: A pair of integers where:
            - First element is the difference between raw string length and evaluated string length
            - Second element is the number of additional characters needed to escape the string

    Example:
        >>> solver('"\\""\n"abc"\n"aaa\\"aaa"\n"\\x27"')
        (12, 16)
    """
    decoded = 0
    encoded = 0

    for string in strings.splitlines():
        encoded += len(string) - len(literal_eval(string))
        decoded += 2 + string.count('\"') + string.count('\\')
    return (encoded, decoded)
