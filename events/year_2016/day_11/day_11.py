"""Advent of Code - Year 2016 - Day 11"""


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
        objects.append(floor.count('microchip') + floor.count('generator'))
    return objects


def solver(objects: list[int]):
    """
    A generator function that solves an elevator optimization problem.

    This function takes an initial state of objects and yields the movement results after two steps:
    1. Making a move with a copy of the initial state
    2. Moving the elevator up 4 floors and making another move

    Args:
        objects (list[int]): List of integers representing the initial state of objects on 
                             different floors.

    Yields:
        The result of each move operation:
        - First yield: Result of move() with copied initial state
        - Second yield: Result of move() after elevator moves up 4 floors
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
