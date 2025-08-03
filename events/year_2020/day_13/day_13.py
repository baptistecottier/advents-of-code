"""
Advent of Code - Year 2020 - Day 13
https://adventofcode.com/2020/day/13
"""

from pythonfw.functions import chinese_remainder


def preprocessing(puzzle_input: str) -> tuple[int, list[int]]:
    """
    Parses the input string to extract the earliest timestamp and a tuple of bus IDs, replacing 'x'
    with 0.
    """
    details = puzzle_input.splitlines()
    timestamp = int(details[0])
    bus = list(int(item) for item in details[1].replace('x', '0').split(','))
    return timestamp, bus


def solver(timestamp: int, bus: list[int]) -> tuple[int, int]:
    """
    Calculates the earliest bus you can take after a given timestamp and the earliest timestamp
    such that all listed bus IDs depart at offsets matching their positions.
    """
    pairs = set()
    times = {}

    for (n, bus_id) in enumerate(bus):
        if bus_id != 0:
            times[-timestamp % bus_id] = bus_id * (-timestamp % bus_id)
            pairs.add((-n, bus_id))
    return times[min(times.keys())], chinese_remainder(pairs)[0]
