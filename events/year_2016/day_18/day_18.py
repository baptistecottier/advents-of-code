"""Advent of Code - Year 2016 - Day 18"""

def preprocessing(puzzle_input: str) -> list[int]:
    """
    Convert puzzle input into a list of booleans with padded zeros.

    Args:
        puzzle_input (str): String of '^' and '.' characters

    Returns:
        list: List of booleans, True for '^' and False for '.'
    """
    return [0] + [int(c == '^') for c in puzzle_input] +  [0]


def solver(tiles: list[int], n_rows: int = 400_000):
    """
    Simulates tile rows and counts safe tiles.

    Args:
        tiles (list[int]): Initial row of tiles, where 1 is a trap and 0 is safe.
        n_rows (int, optional): Number of rows to simulate. Defaults to 400_000.

    Yields:
        int: Number of safe tiles after 40 rows, then after all rows.
    """
    safe_tiles = len(tiles) - sum(tiles) - 2
    for row in range(1, n_rows):
        if row == 40:
            yield safe_tiles
        tiles       = [0] + [tiles[i] ^ tiles[i + 2] for i in range(len(tiles) - 2)] + [0]
        safe_tiles += len(tiles) - sum(tiles) - 2
    yield safe_tiles
