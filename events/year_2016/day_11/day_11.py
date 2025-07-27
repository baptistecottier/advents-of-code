"""
Advent of Code - Year 2016 - Day 11
https://adventofcode.com/2016/day/11
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Process a puzzle input string to count the number of objects per floor.

    This function counts the number of microchips and generators on each floor by scanning
    the input string line by line and counting occurrences of 'microchip' and 'generator'.

    Args:
        puzzle_input (str): A multi-line string describing the objects on each floor

    Returns:
        list[int]: A list where each element represents the total count of objects
                   (microchips + generators) on the corresponding floor
    """
    objects = []
    for floor in puzzle_input.splitlines():
        objects.append(floor.count("microchip") + floor.count("generator"))
    return objects


def solver(objects: list[int]) -> Iterator[int]:
    """
    Solves the puzzle by computing moves for the original configuration and a modified version.

    Args:
        objects: List of integers representing object positions or states.

    Yields:
        int: Results from move operations on original and modified configurations.
    """
    yield move(objects.copy())
    objects[0] += 4
    yield move(objects)


def move(objects: list[int]) -> int:
    """
    Computes the numbers of step to move all elements to the upper floor using a formulae.

    Args:
        objects (list[int]): List of integers to process.

    Returns:
        int: Computed result from the summation formula.
    """
    return sum(2 * sum(objects[:x]) - 3 for x in range(1, 4))
