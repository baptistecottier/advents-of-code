"""
Advent of Code - Year 2020 - Day 5
https://adventofcode.com/2020/day/5
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a string of boarding passes into a sorted list of seat IDs by decoding each pass from
    binary space partitioning format.
    """
    boarding_passes: list = []
    for boarding_pass in puzzle_input.splitlines():
        for src, dst in [("B", "1"), ("F", "0"), ("R", "1"), ("L", "0")]:
            boarding_pass = boarding_pass.replace(src, dst)
        row = int(boarding_pass[:7], 2)
        column = int(boarding_pass[7:], 2)
        boarding_passes.append(8 * row + column)
    return sorted(boarding_passes)


def solver(boarding_passes: list[int]) -> tuple[int, int]:
    """
    Finds the highest seat ID and the first missing seat ID after the lowest in a list of boarding
    passes.
    """
    seat = boarding_passes[0]
    while seat in boarding_passes:
        seat += 1
    return boarding_passes[-1], seat
