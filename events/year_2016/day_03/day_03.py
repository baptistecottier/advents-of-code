"""
Advent of Code - Year 2016 - Day 3
https://adventofcode.com/2016/day/3
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Process raw puzzle input into a list of integers.

    Takes a string of space-separated numbers and converts them into a list of integers.

    Args:
        puzzle_input (str): Raw input string containing space-separated numbers.

    Returns:
        list[int]: List of integers parsed from the input string.

    Examples:
        >>> preprocessing("1 2 3 4 5 6")
        [1, 2, 3, 4, 5, 6]
    """
    return list(map(int, puzzle_input.split()))


def solver(lengths: list[int]) -> Iterator[int]:
    """
    Solve triangle validity problems for different data arrangements.

    Yields the count of valid triangles for each possible interpretation:
    - If lengths divisible by 3: groups consecutive triplets row-wise
    - If lengths divisible by 9: groups by columns in 3x3 blocks

    Args:
        lengths: List of triangle side lengths

    Yields:
        int: Number of valid triangles for each arrangement

    Examples:
        >>> list(solver([3, 4, 5, 1, 2, 10]))  # Valid: (3,4,5), Invalid: (1,2,10)
        [1]
        >>> list(solver([3, 6, 9, 4, 7, 10, 5, 8, 11]))  # 9 elements, both arrangements
        [1, 3]  # Row-wise: 1 valid, Column-wise: 3 valid
    """
    if len(lengths) % 3 == 0:
        triangles = list(lengths[i: i + 3] for i in range(0, len(lengths), 3))
        yield count_possible_triangles(triangles)
    if len(lengths) % 9 == 0:
        triangles = []
        for col in range(3):
            for row in range(0, len(lengths), 9):
                triangles.append(
                    (lengths[row + col], lengths[row + col + 3], lengths[row + col + 6])
                )
        yield count_possible_triangles(triangles)


def count_possible_triangles(triangles: list[list[int]]) -> int:
    """
    Count triangles where the sum of any two sides is larger than the remaining side.

    Args:
        triangles: List of triangle side lengths

    Returns:
        Number of possible triangles

    Examples:
        >>> count_possible_triangles([[5, 10, 25]])
        0
        >>> count_possible_triangles([[3, 4, 5], [1, 1, 3]])
        1
        >>> count_possible_triangles([[3, 4, 5], [6, 8, 10], [1, 2, 3]])
        2
    """
    return sum(sum(triangle) > 2 * max(triangle) for triangle in triangles)
