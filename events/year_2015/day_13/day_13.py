"""Advent of Code - Year 2015 - Day 13"""

from itertools import permutations, pairwise


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Process input string to extract happiness changes.

    Args:
        puzzle_input (str): Raw puzzle input containing happiness changes.

    Returns:
        list[int]: List of integer happiness changes, negative for losses.

    Examples:
        >>> preprocessing("Alice would gain 54 happiness units by sitting next to Bob.")
        [54]
        >>> preprocessing("Alice would lose 79 happiness units by sitting next to Carol.")
        [-79]
        >>> preprocessing("Alice would gain 54 happiness units by sitting next to Bob.
                           Bob would lose 7 happiness units by sitting next to Alice.")
        [54, -7]
    """
    changes = []
    for change in puzzle_input.splitlines():
        gain = int(change.split(' ')[3])
        changes.append(gain if 'gain' in change else - gain)
    return changes


def solver(changes: list[int]) -> tuple[int, int]:
    """
    Solves the seating happiness optimization problem with and without including 'myself'.

    Args:
        changes (list[int]): List of happiness values between each pair of guests.

    Returns:
        tuple[int, int]: Tuple containing optimal happiness without 'myself' and with 'myself'
                         included.

    Examples:
        >>> solver([54, -79, 0, 89]) # Simple case with 2 people
        (143, 89)
        >>> solver([54, -7, 83, -62, 23, -40]) # Case with 3 people
        (128, 108)
    """
    return (compute_changes(changes, myself = False),
            compute_changes(changes, myself = True))


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
        
    Examples:
        >>> compute_changes([54, -7, 83, -62, 23, -40], False)  # 3 people
        128
        >>> compute_changes([54, -7, 83, -62, 23, -40], True)  # 3 people + myself
        108
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
