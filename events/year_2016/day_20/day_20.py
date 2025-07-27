"""
Advent of Code - Year 2016 - Day 20
https://adventofcode.com/2016/day/20
"""


def preprocessing(puzzle_input: str) -> set[tuple[int, int]]:
    """
    Converts puzzle input into a set of blacklisted IP ranges.

    Args:
        puzzle_input (str): Raw puzzle input containing IP ranges

    Returns:
        set[tuple[int, int]]: Set of tuples containing lower and upper bounds of blacklisted ranges
    """
    blacklist = set()
    for element in puzzle_input.splitlines():
        inf, sup = (int(item) for item in element.split("-"))
        blacklist.add((inf, sup))
    return blacklist


def solver(intervales: set[tuple[int, int]], max_val: int = 4_294_967_295) -> tuple[int, int]:
    """
    Find the first allowed IP address and count total allowed IPs within blocked intervals.

    Args:
        intervales: Set of blocked IP ranges as (start, end) tuples
        max_val: Maximum IP address value (default: 4,294,967,295)

    Returns:
        Tuple of (first_allowed_ip, total_allowed_count)

    Examples:
        >>> solver({(5, 8), (0, 2), (4, 7)}, 9)
        (3, 2)
        >>> solver({(0, 0), (2, 2)}, 4)
        (1, 3)
    """
    counter_ip = 0
    allowed_ip = next_allowed_ip(0, intervales)
    first_allowed_ip = allowed_ip
    while allowed_ip <= max_val:
        intervales = set((inf, sup) for (inf, sup) in intervales if sup > allowed_ip)
        min_ip = min(intervales, key=lambda item: item[0], default=[max_val + 1])[0]
        counter_ip += min_ip - allowed_ip
        allowed_ip = next_allowed_ip(min_ip, intervales)
    return first_allowed_ip, counter_ip


def next_allowed_ip(start: int, intervales: set[tuple[int, int]]) -> int:
    """
    Find the next allowed IP address starting from a given position.

    Args:
        start: Starting IP address to check
        intervales: Set of blocked IP ranges as (min, max) tuples (inclusive)

    Returns:
        First IP address >= start that is not in any blocked range

    Examples:
        >>> next_allowed_ip(0, {(0, 2), (5, 7)})
        3
        >>> next_allowed_ip(10, {(0, 2), (5, 7)})
        10
        >>> next_allowed_ip(1, {(0, 5), (6, 10)})
        11
    """
    for inf, sup in intervales:
        if start in range(inf, sup + 1):
            intervales = set((inf, sup) for (inf, sup) in intervales if sup > start)
            return next_allowed_ip(sup + 1, intervales)
    return start
