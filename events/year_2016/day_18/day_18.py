"""
Advent of Code - Year 2016 - Day 18
https://adventofcode.com/2016/day/18
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Convert puzzle input into a list of integers with padded zeros.

    Args:
        puzzle_input (str): String of '^' and '.' characters

    Returns:
        list[int]: List of integers, 1 for '^' and 0 for '.'

    Example:
        >>> preprocessing("^^.^")
        [0, 1, 1, 0, 1, 0]
    """
    return [0] + [int(c == "^") for c in puzzle_input] + [0]


def solver(tiles: list[int], n_rows: int = 400_000) -> Iterator[int]:
    """
    Generates safe tile counts for a trapping puzzle with evolving rows.

    Each row is generated from the previous using XOR logic on adjacent tiles.
    Safe tiles are represented by 0, traps by 1.

    Args:
        tiles (list[int]): Initial row configuration (0=safe, 1=trap)
        n_rows (int): Total rows to process (default: 400,000)

    Yields:
        int: Safe tile count at row 40, then final count after all rows

    Example:
        >>> list(solver([0, 1, 1, 0, 1, 0], 3))
        [6, 6]
    """
    safe_tiles = len(tiles) - sum(tiles) - 2
    for row in range(1, n_rows):
        if row == 40:
            yield safe_tiles
        tiles = [0] + [tiles[i] ^ tiles[i + 2] for i in range(len(tiles) - 2)] + [0]
        safe_tiles += len(tiles) - sum(tiles) - 2
    yield safe_tiles
