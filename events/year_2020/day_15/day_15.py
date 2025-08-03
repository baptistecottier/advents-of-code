"""
Advent of Code - Year 2020 - Day 15
https://adventofcode.com/2020/day/15
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> tuple[dict[int, list[int]], int]:
    """
    Parses a comma-separated string of integers into a dictionary mapping each number to its
    positions and returns the dictionary along with the last number.
    """
    values = [int(item) for item in puzzle_input.split(',')]
    return ({spoken: [n] for (n, spoken) in enumerate(values)}, values[-1])


def solver(spoken: dict[int, list[int]], last_spoken: int) -> Iterator[int]:
    """
    Generates the number spoken at turn 2020 and at turn 30,000,000 in a memory game sequence based
    on initial spoken numbers.
    """
    for i in range(len(spoken), 30_000_000):
        if i == 2_020:
            yield last_spoken

        if len(spoken[last_spoken]) == 1:
            last_spoken = 0
        else:
            p, n = spoken[last_spoken]
            last_spoken = n - p

        if last_spoken in spoken:
            spoken[last_spoken] = [spoken[last_spoken][-1], i]
        else:
            spoken[last_spoken] = [i]

    yield last_spoken
