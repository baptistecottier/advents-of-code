"""
Advent of Code - Year 2015 - Day 2
https://adventofcode.com/2015/day/2
"""

from dataclasses import dataclass


@dataclass
class Box:
    """
    A class representing a box with length, width, and height dimensions.

    Attributes:
        l (int): The length of the box
        w (int): The width of the box
        h (int): The height of the box
    """

    l: int
    w: int
    h: int


def preprocessing(puzzle_input: str) -> list[Box]:
    """
    Parse puzzle input into a list of Box objects with sorted dimensions.

    Args:
        puzzle_input: String containing box dimensions in 'lxwxh' format.

    Returns:
        List of Box objects with dimensions sorted in ascending order.

    Raises:
        ValueError: If input doesn't match the expected format.

    Examples:
        >>> preprocessing("2x3x4")
        [Box(l=2, w=3, h=4)]

        >>> preprocessing("1x1x10\\n2x3x4")
        [Box(l=1, w=1, h=10), Box(l=2, w=3, h=4)]
    """
    boxes = []
    for box in puzzle_input.splitlines():
        try:
            l, w, h = sorted(list(map(int, box.split("x"))))
            boxes.append(Box(l, w, h))
        except Exception as e:
            raise ValueError(
                f"Wrong input format: {box}.Expected format is 'lxwxh'"
            ) from e
    return boxes


def solver(boxes: list[Box]) -> tuple[int, int]:
    """
    Calculate the total wrapping paper and ribbon needed for all boxes.

    Args:
        boxes: List of Box objects with dimensions l, w, and h

    Returns:
        tuple: (total paper needed, total ribbon needed)

    Examples:
        >>> solver([Box(l=2, w=3, h=4)])
        (58, 34)

        >>> solver([Box(l=1, w=1, h=10)])
        (43, 14)

        >>> solver([Box(l=2, w=3, h=4), Box(l=1, w=1, h=10)])
        (101, 48)
    """
    paper = 0
    ribbon = 0

    for box in boxes:
        preprod = box.l * box.w
        presum = 2 * (box.l + box.w)
        paper += 3 * preprod + presum * box.h
        ribbon += box.h * preprod + presum

    return paper, ribbon
