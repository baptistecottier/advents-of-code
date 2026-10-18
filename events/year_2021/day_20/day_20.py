"""
Advent of Code - Year 2021 - Day 20
https://adventofcode.com/2021/day/20
"""

# Standard imports
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> tuple[set[int], set[tuple[int, int]]]:
    """
    Returns the indices of the '#' characters of the image enhancement algorithm, and the
    coordinates (x, y) of the lit pixels of the input image.
    """
    sections = puzzle_input.split('\n\n')

    enhancement = {n for n, p in enumerate(sections[0].replace('\n', '')) if p == '#'}
    light_pixels = set()
    for y, line in enumerate(sections[1].splitlines()):
        for x, pixel in enumerate(line):
            if pixel == '#':
                light_pixels.add((x, y))
    return enhancement, light_pixels


def solver(enhancement: set[int], pixels: set[tuple[int, int]]) -> Iterator[int]:
    """
    Yields the number of lit pixels after 2 enhancement rounds, then after 50. Each pixel is
    updated from the 9-bit index of its 3x3 window, built incrementally down each column.
    When the first character of the algorithm is '#', the infinite background flips every
    round, so pixels alternately holds the dark pixels (while dark is True) and the lit ones.
    """
    rounds = 50
    x_min = min(x for x, _ in pixels)
    x_max = max(x for x, _ in pixels)
    y_min = min(y for _, y in pixels)
    y_max = max(y for _, y in pixels)

    en0 = 0 in enhancement
    dark = False
    for r in range(1, 1 + rounds):
        updated_pixels = set()
        for x in range(x_min - 2 * r, x_max + 2 * r):
            idx = init_idx(x, y_min - 2 * r, pixels)
            if dark:
                idx ^= 63
            for y in range(y_min - 2 * r, y_max + 2 * r):
                for node in ((x - 1, y + 1), (x, y + 1), (x + 1, y + 1)):
                    idx = (idx << 1) | ((node in pixels) ^ dark)
                idx %= 512
                if (idx in enhancement) ^ (en0 and not dark):
                    updated_pixels.add((x, y))

        pixels = updated_pixels
        if r == 2:
            yield len(pixels)
        if en0:
            dark = not dark
    yield len(pixels)


def init_idx(x: int, y_min: int, pixels: set[tuple[int, int]]) -> int:
    """
    Returns the 6-bit index of rows y_min - 1 and y_min over columns x - 1 to x + 1, read left
    to right and top to bottom, a bit being set when its position is in pixels. These are the
    first two rows of the window centered on (x, y_min), which the solver completes.
    """
    idx = 0
    for node in ((x - 1, y_min - 1), (x, y_min - 1), (x + 1, y_min - 1),
                 (x - 1, y_min), (x, y_min), (x + 1, y_min)):
        idx = (idx << 1) | (node in pixels)
    return idx
