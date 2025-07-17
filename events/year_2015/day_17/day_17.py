"""Advent of Code - Year 2015 - Day 17"""

from itertools import combinations


def preprocessing(puzzle_input: str) -> tuple[int, ...]:
    """
    Process input into tuple of container sizes.

    Args:
        puzzle_input (str): Raw puzzle input string with container sizes.

    Returns:
        tuple[int]: Container sizes as integers.

    Examples:
        >>> preprocessing("20\\n15\\n10\\n5\\n5")
        (20, 15, 10, 5, 5)

        >>> preprocessing("10\\n20\\n30")
        (10, 20, 30)
    """
    return tuple(int(container) for container in puzzle_input.splitlines())


def solver(*containers: tuple[int], liters: int = 150) -> tuple[int, int]:
    """
    Calculate the number of container combinations for a specific volume.

    Args:
        containers: A variable-length tuple of container sizes (integers).
        liters: The target volume to be reached (default: 150).

    Returns:
        tuple: A tuple containing:
            - The total number of valid combinations
            - The number of valid combinations with the minimum number of containers

    Examples:
        >>> solver(20, 15, 10, 5, 5, liters=25)
        (4, 3)  # 4 total combinations, 3 minimum-container combinations

        >>> solver(10, 20, 30, 40, 50, liters=50)
        (3, 1)  # 3 total combinations, 1 minimum-container combination
    """
    combin = []

    for size in range(len(containers)):
        size_total = 0
        for comb in combinations(containers, size):
            if sum(comb, start=0) == liters:
                size_total += 1
        if size_total != 0:
            combin.append(size_total)

    return sum(combin), combin[0]
