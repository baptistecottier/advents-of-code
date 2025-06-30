"""Advent of Code - Year 2017 - Day 01"""

def preprocessing(puzzle_input: str) -> list[int]:
    """
    Convert string input into list of integers.

    Args:
        puzzle_input (str): Input string containing digits.

    Returns:
        list[int]: List of integers parsed from input string.
    """
    return list(map(int, puzzle_input))


def solver(captcha: list[int]):
    """Solves the captcha puzzle by finding matching digits in a circular list.

    This function takes a list of digits and returns a tuple of two sums:
    1. Sum of digits that match the next digit in the circular list
    2. Sum of digits that match the digit halfway around the circular list

    Args:
        captcha (list[int]): A list of integers representing the captcha sequence

    Returns:
        tuple[int, int]: A tuple containing:
            - First sum: matches with next digit
            - Second sum: matches with halfway digit
    """
    return (sum_matches(captcha, 1),
            sum_matches(captcha, len(captcha) // 2))


def sum_matches(captcha: list[int], delta: int):
    """
    Returns the sum of elements in 'captcha' that match the element 'delta' positions ahead,
    wrapping around the list.
    """
    return sum(a for (a, b) in zip(captcha, captcha[delta:] + captcha[:delta]) if a == b)
