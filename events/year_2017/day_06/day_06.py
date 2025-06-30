"""Advent of Code - Year 2017 - Day 06"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Convert puzzle inoput in a list of int
    
    Exemple
        >>> preprocessing("2 4 1 2")
        [2, 4, 1, 2]
    """
    return list(int(item) for item in puzzle_input.split())


def solver(state: list[int]):
    """
    Solves memory bank redistribution problem by finding cycles.
    
    Args:
        state (list[int]): Initial memory banks state
        
    Yields:
        int: Number of steps before cycle
        int: Length of cycle
    """
    visited, last = redistributions(state)
    cycles = len(visited)
    yield cycles
    yield cycles - visited.index(last)


def redistributions(bank):
    """
    Redistributes memory blocks until a repeated configuration is found.
    
    Args:
        bank (list): A list of integers representing memory blocks.
        
    Returns:
        tuple: (seen, bank) where 'seen' is a list of all configurations before the repeat
               and 'bank' is the first repeated configuration.
    """
    n   = len(bank)
    seen = []

    while bank not in seen:
        seen.append(bank.copy())
        to_distribute = max(bank)
        i = bank.index(to_distribute)
        bank[i] = 0
        for j in range(n):
            bank[j] += to_distribute // n + ((j - (i + 1)) % n < (to_distribute % n))
    return seen, bank
