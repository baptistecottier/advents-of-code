"""Advent of Code - Year 2016 - Day 20"""

def preprocessing(puzzle_input: str) -> set[tuple[int, int]]:
    """Converts puzzle input into a set of blacklisted IP ranges.

    Args:
        puzzle_input (str): Raw puzzle input containing IP ranges

    Returns:
        set[tuple[int, int]]: Set of tuples containing lower and upper bounds of blacklisted ranges
    """
    blacklist = set()
    for element in puzzle_input.splitlines():
        inf, sup = (int(item) for item in element.split('-'))
        blacklist.add((inf, sup))
    return blacklist


def solver(intervales: set[tuple[int, int]], max_val: int = 4_294_967_295):
    """
    Yields the first allowed IP and then the count of allowed IPs not covered by given intervals.

    Args:
        intervales (set[tuple[int, int]]): Set of (start, end) tuples representing blocked IP 
                                           ranges.
        max_val (int, optional): Maximum IP value to consider. Defaults to 4_294_967_295.

    Yields:
        int: The first allowed IP address.
        int: The total number of allowed IP addresses.
    """
    counter_ip = 0
    allowed_ip =next_allowed_ip(0, intervales)
    yield allowed_ip
    while allowed_ip <= max_val:
        intervales  = set((inf , sup) for (inf , sup) in intervales if sup > allowed_ip)
        min_ip      = min(intervales, key = lambda item: item[0], default=[max_val + 1])[0]
        counter_ip += min_ip - allowed_ip
        allowed_ip  = next_allowed_ip(min_ip, intervales)
    yield counter_ip


def next_allowed_ip(start: int, intervales: set[tuple[int, int]]) -> int:
    """
    Find the next IP address that is not within any blocked interval.

    This function recursively searches for the first allowed IP address starting from 
    a given value, considering a list of blocked IP ranges.

    Args:
        start (int): The IP address to start searching from
        intervales (list[tuple[int, int]]): List of tuples containing (lower, upper) bounds 
            of blocked IP ranges

    Returns:
        int: The next allowed IP address that doesn't fall within any blocked range

    Example:
        >>> intervals = [(5,8), (0,2), (4,7)]
        >>> next_allowed_ip(1, intervals)
        3
    """
    for inf, sup in intervales:
        if start in range(inf, sup + 1):
            intervales = set((inf, sup) for (inf, sup) in intervales if sup > start)
            return next_allowed_ip(sup + 1 ,intervales)
    return start
