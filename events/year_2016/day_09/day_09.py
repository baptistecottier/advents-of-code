"""
Advent of Code - Year 2016 - Day 9
https://adventofcode.com/2016/day/9
"""

from collections.abc import Iterator
from parse import parse, Result


def solver(file: str) -> Iterator[int]:
    """
    Solve the decompression puzzle for both non-recursive and recursive modes.

    Args:
        file (str): The compressed string to decompress.

    Yields:
        int: Decompressed file size for non-recursive mode, then recursive mode.

    Examples:
        >>> list(solver("A(1x5)BC"))
        [7, 7]
        >>> list(solver("X(8x2)(3x3)ABCY"))
        [20, 36]
    """
    for recursivity in [False, True]:
        yield get_file_size(file, recursivity)


def get_file_size(file: str, recursivity: bool) -> int:
    """
    Calculate the decompressed size of a file with compression markers.

    Args:
        file (str): The compressed file content as a string
        recursivity (bool): Whether to recursively decompress nested markers

    Returns:
        int: The total size of the decompressed file

    Raises:
        ValueError: If the compression marker format is invalid

    Examples:
        >>> get_file_size("A(1x5)BC", False)
        7
        >>> get_file_size("A(2x2)BCD(2x2)EFG", False)
        11
    """
    for i, c in enumerate(file):
        if c == "(":
            result = parse("({:d}x{:d}){}", file[i:])
            if isinstance(result, Result):
                width, rep, _ = result
                length = i + len(str(width) + str(rep)) + 3
                size = i + get_file_size(file[length + width:], recursivity)
                if recursivity is True:
                    return size + rep * get_file_size(
                        file[length: length + width], True
                    )
                return size + rep * len(file[length: length + width])
            raise ValueError("Incorrect input format. I can not decompress your file")
    return len(file)
