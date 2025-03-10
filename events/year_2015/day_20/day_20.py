"""Advent of Code - Year 2015 - Day 20"""

from math import sqrt


def solver(str_target: str):
    """Find the lucky house numbers based on target value.

    Args:
        str_target (str): Target number as string to find houses for

    Yields:
        int: First house number meeting condition with infinite elves
        int: First house number meeting condition with limited elves
    """
    target = int(str_target)
    yield find_lucky_house(target // 10, lambda n: 1 + int(sqrt(n)))
    yield find_lucky_house(target // 11, lambda _: 50)


def find_lucky_house(target: int, bound: callable) -> int:
    """
    Find the house number where the sum of bounded divisors first exceeds the target.

    Args:
        target: The minimum sum of presents to find.
        bound: A callable that determines the upper bound for divisors.

    Returns:
        The house number (smallest) where the sum of presents reaches the target.
    """
    n = 210
    while bounded_divisors_sum(n, bound) < target:
        n += 210
    return n


def bounded_divisors_sum(n: int, bound: callable) -> int:
    """
    Calculates the sum of divisors of n and their quotients, up to a bound.
    """
    return sum(k + (n // k) for k in range(1, 1 + bound(n)) if n % k == 0)
