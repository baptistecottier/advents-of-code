"""Advent of Code - Year 2016 - Day 09"""

from parse import parse, Result


def solver(file: str):
    """
    Solves Part 1 and Part 2 of Day 9 puzzle.

    This function processes a file containing a compressed sequence and yields two values:
    1. The decompressed length when markers are processed only once (Part 1)
    2. The decompressed length when markers are processed recursively (Part 2)

    Args:
        file (str): Path to the input file containing the compressed sequence

    Yields:
        int: The length of the decompressed sequence for Part 1
        int: The length of the decompressed sequence for Part 2
    """
    yield get_file_size(file, False)
    yield get_file_size(file, True)


def get_file_size(file: str, recursivity: bool) -> int:
    """
    Calculates the decompressed size of a file string using marker-based expansion.

    Args:
        file (str): The input string representing the compressed file.
        recursivity (bool): If True, recursively decompresses markers within markers. If False, only
            decompresses top-level markers.

    Returns:
        int: The total length of the decompressed file.

    Notes:
        Markers in the input string are of the form (AxB), meaning the next A characters should be
        repeated B times. If recursivity is enabled, nested markers are also expanded recursively.
    """
    for i, c in enumerate(file):
        if c == '(':
            result = parse('({:d}x{:d}){}', file[i:])
            if isinstance(result, Result):
                width, rep, _ = result
                length = i + len(str(width) + str(rep)) + 3
                size = i + get_file_size(file[length + width:], recursivity)
                if recursivity is True:
                    return size + rep * get_file_size(file[length: length + width], True)
                return size + rep * len(file[length: length + width])
            else:
                raise ValueError("Incorrect input format. I can not decompress your file")
    return len(file)
