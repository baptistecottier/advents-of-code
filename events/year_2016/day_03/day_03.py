"""Advent of Code - Year 2016 - Day 03"""

def preprocessing(puzzle_input: str) -> list[int]:
    """Process raw puzzle input into a list of integers.

    Takes a string of space-separated numbers and converts them into a list of integers.

    Args:
        puzzle_input (str): Raw input string containing space-separated numbers.

    Returns:
        list[int]: List of integers parsed from the input string.
    """
    return list(map(int, puzzle_input.split()))


def solver(lengths: list[int]):
    """
    Solves two triangle counting problems based on the input list of side lengths.

    Given a flat list of side lengths, this function yields the number of possible triangles in two
    ways:
    1. If the list length is a multiple of 3, it groups every three consecutive lengths as a triangle
        and yields the count of valid triangles.
    2. If the list length is a multiple of 9, it also considers triangles formed by taking columns from
        each group of three rows (i.e., every 3rd element in blocks of 9), and yields the count of valid
        triangles for this arrangement.

    If neither condition is met, yields None.

    Args:
         lengths (list[int]): A flat list of side lengths.

    Yields:
         int or None: The number of possible triangles for each arrangement, or None if input length is
         invalid.
    """
    if len(lengths) % 3 == 0:
        triangles = list(lengths[i: i + 3] for i in range(0, len(lengths), 3))
        yield count_possible_triangles(triangles)
    if len(lengths) % 9 == 0:
        triangles = []
        for col in range(3):
            for row in range(0, len(lengths), 9):
                triangles.append((lengths[row + col    ],
                                  lengths[row + col + 3],
                                  lengths[row + col + 6]))
        yield count_possible_triangles(triangles)
    else:
        yield None


def count_possible_triangles(triangles: list[list[int]]) -> int:
    """Count triangles where the sum of any two sides is larger than the remaining side.
    Args:
        triangles: List of triangle side lengths
    Returns:
        Number of possible triangles
    """
    return sum(sum(triangle) > 2 * max(triangle) for triangle in triangles)
