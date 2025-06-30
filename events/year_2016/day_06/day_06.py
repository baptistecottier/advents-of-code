"""Advent of Code - Year 2016 - Day 06"""

from collections import Counter


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Process input string into list of lines.

    Args:
        data (str): Raw input data

    Returns:
        list[str]: List of lines from input
    """
    return puzzle_input.splitlines()


def solver(messages: list[str]):
    """
    Decodes a list of equal-length message strings by determining the most and least common character
    at each position.

    Args:
        messages (list[str]): A list of strings, each representing a message of equal length.

    Returns:
        tuple[str, str]: A tuple containing two strings:
            - The first string is formed by concatenating the most common character at each position.
            - The second string is formed by concatenating the least common character at each position.

    Example:
        >>> solver(["eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev", "sdttsa", "rasrtv",
        ...         "nssdts", "ntnada", "svetve", "tesnvt", "vntsnd", "vrdear", "dvrsen", "enarar"])
        ('easter', 'advent')
    """
    most_commons = ""
    least_commons = ""
    for i in range(len(messages[0])):
        letters = (message[i] for message in messages)
        cntr = Counter(letters).most_common()
        most_commons  += cntr[0][0]
        least_commons += cntr[-1][0]
    return most_commons, least_commons
