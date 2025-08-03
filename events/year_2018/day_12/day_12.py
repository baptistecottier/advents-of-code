"""
Advent of Code - Year 2018 - Day 12
https://adventofcode.com/2018/day/12
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> tuple[str, dict[str, str]]:
    """
    Parse puzzle input to extract initial state and transformation rules.
    """
    state, comb = puzzle_input.split('\n\n')
    state = state.split(': ')[1]
    combinations = {}
    for c in comb.splitlines():
        prev, post = c.split(' => ')
        combinations[prev] = post
    return state, combinations


def solver(state: str, spread: dict[str, str]) -> Iterator[int]:
    """
    Solves plant growth simulation by detecting convergence patterns.

    Args:
        state (str): Initial plant configuration string
        spread (dict[str, str]): Rules mapping patterns to growth outcomes

    Yields:
        int: Sum at generation 20, then extrapolated sum at generation 50B

    Examples:
        >>> list(solver("##..#", {"##...": "#", "..#..": "."}))
        [325, 2000000001325]
    """
    previous_sum = sum_pots(previous_state := generate(state, spread), 1)
    current_sum = sum_pots(current_state := generate(previous_state, spread), 2)
    next_sum = sum_pots(next_state := generate(current_state, spread), n := 3)
    cycles = 0

    while 2 * current_sum != next_sum + previous_sum:
        cycles += 1
        if cycles == 19:
            yield current_sum
        previous_sum, current_sum = current_sum, next_sum
        next_sum = sum_pots(next_state := generate(next_state, spread), n := n + 1)
    yield next_sum + (next_sum - current_sum) * (50_000_000_000 - n)


def generate(state: str, spread: dict[str, str]) -> str:
    """
    Generates the next state of plants based on current state and spread rules.
    """
    return ''.join([spread['.' * (5 - n) + state[:n]] for n in range(1, 5)] +
                   [spread[state[n: n + 5]] for n in range(len(state) - 4)] +
                   [spread[state[n - 5:] + '.' * n] for n in range(1, 5)])


def sum_pots(state: str, generations: int) -> int:
    """
    Calculate the sum of pot positions containing plants, adjusted for generation offset.
    """
    return sum(i - 2 * generations for i, p in enumerate(state) if p == '#')
