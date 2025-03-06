"""Advent of Code - Year 2015 - Day 04"""

from pythonfw.functions import md5


def solver(target: str):
    """Find the lowest positive number that produces an MD5 hash starting with specified zeros.

    This function iterates through numbers to find the smallest one that, when appended to
    the target string and hashed using MD5, produces a hash starting with either five or six zeros.

    Args:
        target (str): The input string to which numbers will be appended before hashing.

    Yields:
        int: First yields the lowest number that produces a hash starting with five zeros,
             then yields the lowest number that produces a hash starting with six zeros.

    Example:
        >>> list(solver("abcdef"))
        [609043, 6742839]
    """
    counter = 0
    for trigger in ['00000', '000000']:
        while not md5(f"{target}{counter}").startswith(trigger):
            counter += 1
        yield counter
