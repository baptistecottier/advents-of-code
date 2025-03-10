"""Advent of Code - Year 2015 - Day 13"""

from itertools import permutations, pairwise


def preprocessing(puzzle_input: str) -> list[int]:
    """Process input string to extract happiness changes.

    Args:
        puzzle_input (str): Raw puzzle input containing happiness changes.

    Returns:
        list[int]: List of integer happiness changes, negative for losses.
    """
    changes = []
    for change in puzzle_input.splitlines():
        gain = int(change.split(' ')[3])
        changes.append(gain if 'gain' in change else - gain)
    return changes


def solver(changes: list[int]):
    """
    Solves the seating happiness optimization problem with and without including 'myself'.

    Args:
        changes (list[int]): List of happiness values between each pair of guests.

    Yields:
        int: First yield is optimal happiness without 'myself', second with 'myself' included.
    """
    yield compute_changes(changes, myself = False)
    yield compute_changes(changes, myself = True)


def compute_changes(changes: list[int], myself: bool) -> int:
    """
    Compute the optimal arrangement of people to maximize happiness changes.

    This function calculates the maximum possible happiness score by trying all possible 
    seating arrangements in a circular table. Each person's happiness is affected by who
    they sit next to.

    Parameters:
        changes (list[int]): List of happiness changes. For n people, contains n*(n-1) values
                            representing how much happiness each person would gain/lose sitting
                            next to each other person.
        myself (bool): Whether to include yourself in the seating arrangement.
                      When True, adds an extra person with 0 happiness impact.

    Returns:
        int: Maximum total happiness achievable from the optimal seating arrangement.
    """
    n = 1 + int((len(changes)**.5)) + myself
    best = 0
    for arrangement in permutations(range(n)):
        acc = 0
        for (a, b) in pairwise(arrangement + (arrangement[0],)):
            if n - myself in (a, b):
                continue
            i1 = (n - 1 - myself) * a + b - (b > a)
            i2 = (n - 1 - myself) * b + a - (a > b)
            acc += changes[i1] + changes[i2]
        best = max(best, acc)
    return best
