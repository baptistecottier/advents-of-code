"""
Advent of Code - Year 2025 - Day 12
https://adventofcode.com/2025/day/12
"""


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Parses the puzzle input string into a list of regions, each represented as [width, length,
    presents].
    """

    grids = puzzle_input.split('\n\n')[-1]

    regions = []
    for grid in grids.splitlines():
        data = grid.split()
        width, length = tuple(map(int, data[0][:-1].split('x')))
        presents = list(map(int, data[1:]))
        regions.append([width, length, presents])
    return regions


def solver(regions: list[tuple[int, int, list[int]]]) -> int:
    """
    Calculates the number of regions where the sum of the elements in the list `p` multiplied by 9
    does not exceed the product of `w` and `l`.
    """
    return sum(sum(p) * 9 <= w * l for w, l, p in regions)
