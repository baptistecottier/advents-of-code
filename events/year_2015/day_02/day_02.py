"""Advent of Code - Year 2015 - Day 02"""

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
    """Process raw puzzle input into a list of Box objects.

    Takes a string containing box dimensions in the format 'lxwxh' (length x width x height)
    per line and converts it into Box objects. Dimensions are sorted in ascending order.

    Args:
        puzzle_input (str): Raw input string with box dimensions, one per line in 'lxwxh' format

    Returns:
        list[Box]: List of Box objects created from the input dimensions

    Raises:
        ValueError: If input format is invalid for any box specification

    Example:
        >>> preprocessing("2x3x4\n1x1x10")
        [Box(l=2, w=3, h=4), Box(l=1, w=1, h=10)]
    """
    boxes = []
    for box in puzzle_input.splitlines():
        try:
            l, w, h = sorted(list(map(int, box.split('x'))))
            boxes.append(Box(l, w, h))
        except Exception as e:
            raise ValueError(f"Wrong input format: {box}.Expected format is 'lxwxh'") from e
    return boxes


def solver(boxes: list[Box]):
    """Calculate total wrapping paper and ribbon needed for all boxes.

    Computes the required amount of wrapping paper and ribbon for a list of boxes.
    For each box, calculates:
    - Paper: 3 * (l * w) + 2 * (l + w) * h
    - Ribbon: h * (l * w) + 2 * (l + w)

    Args:
        boxes (list[Box]): List of Box objects containing length (l), width (w), and height (h)

    Yields:
        int: Total square feet of wrapping paper needed
        int: Total feet of ribbon needed 
    """
    paper  = 0
    ribbon = 0

    for box in boxes:
        preprod = box.l * box.w
        presum  = 2 * (box.l + box.w)
        paper  += 3 * preprod + presum * box.h
        ribbon += box.h * preprod + presum

    yield paper
    yield ribbon
