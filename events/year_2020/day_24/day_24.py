"""
Advent of Code - Year 2020 - Day 24
https://adventofcode.com/2020/day/24
"""


def preprocessing(puzzle_input: str) -> set[tuple[int, int]]:
    """
    Parses a string of tile movement instructions and returns a set of coordinates representing
    flipped tiles.
    """
    tiles = set()

    for tile in puzzle_input.splitlines():
        n = {}
        for value in ['se', 'sw', 'ne', 'nw', 'e', 'w']:
            n[value] = tile.count(value)
            tile = tile.replace(value, '')
        x = n['e'] - n['w'] + 0.5 * (n['se'] + n['ne']) - 0.5 * (n['sw'] + n['nw'])
        y = n['nw'] + n['ne'] - (n['sw'] + n['se'])
        if (x, y) in tiles:
            tiles.remove((x, y))
        else:
            tiles.add((x, y))

    return tiles


def solver(tiles: set[tuple[int, int]]):
    """
    Simulates 100 iterations of a tile-flipping process on a hexagonal grid and returns the initial
    and final counts of black tiles.
    """
    initial_tiles_size = len(tiles)

    neighbours = {(0.5, -1), (-0.5, -1), (0.5, 1), (-0.5, 1), (1, 0), (-1, 0)}
    for _ in range(100):
        tested = set()
        updated_tiles = set()
        for x, y in tiles:
            if sum((x + dx, y + dy) in tiles for dx, dy in neighbours) in [1, 2]:
                updated_tiles.add((x, y))
            for tx, ty in neighbours:
                x2 = x + tx
                y2 = y + ty
                if (x2, y2) not in tiles and (x2, y2) not in tested:
                    tested.add((x2, y2))
                    if sum((x2 + dx, y2 + dy) in tiles for dx, dy in neighbours) == 2:
                        updated_tiles.add((x2, y2))
        tiles = updated_tiles
    return initial_tiles_size, len(tiles)
