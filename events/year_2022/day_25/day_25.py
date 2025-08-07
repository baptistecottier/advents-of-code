"""
Advent of Code - Year 2022 - Day 25
https://adventofcode.com/2022/day/25
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Splits the input puzzle string into a list of lines.
    """
    return puzzle_input.splitlines()


def solver(snafus: list[str]) -> Iterator[str]:
    """
    Yields the decoded result of the sum of encoded SNAFU numbers from the input list.
    """
    to_supply = sum(encode(snafu) for snafu in snafus)
    yield decode(to_supply)


def encode(snafu: str) -> int:
    """
    Converts a list of SNAFU digits (as strings) to its corresponding integer value.
    """
    n = 0
    size = len(snafu)
    for index, c in enumerate(snafu, 1):
        match c:
            case '=': c = -2
            case '-': c = -1
            case '0': c = 0
            case '1': c = 1
            case '2': c = 2
        n += c * 5 ** (size - index)
    return n


def decode(decimal: int) -> str:
    """
    Converts a decimal integer to its SNAFU numeral system string representation.
    """
    numbers = []
    while decimal:
        numbers.append(decimal % 5)
        decimal //= 5
    for index, number in enumerate(numbers):
        if number > 2:
            number -= 5
            if index + 1 == len(numbers):
                numbers.append(1)
            else:
                numbers[index + 1] += 1
    return ''.join('=-012'[n + 2] for n in numbers[::-1])
