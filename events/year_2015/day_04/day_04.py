"""
Advent of Code - Year 2015 - Day 4
https://adventofcode.com/2015/day/4
"""

# Stabdard imports
from collections.abc import Iterator

# First-party imports
from pythonfw.functions import md5


def solver(target: str) -> Iterator[int]:
    """
    Find values that produce MD5 hashes with specific prefixes when combined with target.

    Iteratively finds integers that, when appended to 'target', produce MD5 hashes starting with
    '00000' (first yield) and '000000' (second yield).

    Args:
        target: The string prefix to combine with counter values for hashing.

    Yields:
        Integers that produce MD5 hashes with the required number of leading zeros.

    Examples:
        >>> list(solver("abcdef"))  # Both numbers for '00000' and '000000'
        [609043, 6742839]
        >>> next(solver("pqrstuv"))  # Another example from the problem
        1048970
    """
    counter = 0
    for trigger in ["00000", "000000"]:
        while not md5(f"{target}{counter}").startswith(trigger):
            counter += 1
        yield counter
