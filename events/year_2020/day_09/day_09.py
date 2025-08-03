"""
Advent of Code - Year 2020 - Day 9
https://adventofcode.com/2020/day/9
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a multiline string of numbers into a list of integers.
    """
    return list(map(int, puzzle_input.splitlines()))


def solver(data: list[int], preamble_size=25) -> tuple[int, int]:
    """
    Finds the first number in the list that is not the sum of two of the previous 'preamble_size'
    numbers and returns it along with the sum of the smallest and largest numbers in a contiguous
    range that sums to this number.
    """
    index = preamble_size
    target = data[index]
    preamble = data[:preamble_size]

    while any(target - p in preamble for p in preamble):
        index += 1
        target = data[index]
        preamble = data[index - preamble_size: index]

    for index in range(len(data)):
        vrange = data[index:][::-1]
        values = []
        while sum(values) < target:
            values.append(vrange.pop())
        if sum(values) == target:
            return target, min(values) + max(values)
    raise ValueError("No encryption weakness found")
