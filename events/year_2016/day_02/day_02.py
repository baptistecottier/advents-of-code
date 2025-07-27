"""
Advent of Code - Year 2016 - Day 2
https://adventofcode.com/2016/day/2
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Splits the input string into a list of lines.

    Args:
        puzzle_input (str): The input string to process.

    Returns:
        list[str]: A list of strings, each representing a line from the input.

    Example:
        >>> preprocessing("line1\nline2\nline3")
        ['line1', 'line2', 'line3']
    """
    return puzzle_input.splitlines()


def solver(procedure: list[str]) -> Iterator[str]:
    """
    Yields the results of applying different keypad functions to a list of instructions.

    Args:
        procedure (list[str]): A list of movement instructions.

    Yields:
        str: The result from each keypad function.

    Example:
        >>> list(solver(['ULL', 'RRDDD', 'LURDL', 'UUUUD']))
        ['1985', '5DB3']
    """
    for keypad in squared_keypad, diamond_keypad:
        yield keypad(procedure)


def squared_keypad(procedures: list[str]) -> str:
    """
    Computes the code for a standard 3x3 keypad based on movement instructions.

    Each procedure is a string of directions ('U', 'D', 'L', 'R') that moves a finger on the keypad:
        1 2 3
        4 5 6
        7 8 9

    The starting position is 5. After each procedure, the current digit is appended to the code.

    Args:
        procedures (list[str]): List of strings, each containing movement instructions.

    Returns:
        str: The resulting code after following all procedures.

    Example:
        >>> squared_keypad(["ULL", "RRDDD", "LURDL", "UUUUD"])
        '1985'
    """
    code = ""
    position = 5
    for procedure in procedures:
        for instruction in procedure:
            match instruction, position:
                case ["D", (1 | 2 | 3 | 4 | 5 | 6)]:
                    position += 3
                case ["U", (4 | 5 | 6 | 7 | 8 | 9)]:
                    position -= 3
                case ["L", (2 | 3 | 5 | 6 | 8 | 9)]:
                    position -= 1
                case ["R", (1 | 2 | 4 | 5 | 7 | 8)]:
                    position += 1
        code += format(position)
    return code


def diamond_keypad(procedures: list[str]) -> str:
    """
    Computes the code for a diamond-shaped keypad based on movement procedures.

    The keypad layout is:
        1
      2 3 4
    5 6 7 8 9
      A B C
        D

    Each procedure is a string of instructions ('U', 'D', 'L', 'R') that moves a finger on the
    keypad. The starting position is 5, and after each procedure, the current position is appended
    (in hexadecimal) to the code.

    Args:
        procedures (list[str]): List of movement instruction strings.

    Returns:
        str: The resulting code as a string of hexadecimal digits.

    Example:
        >>> diamond_keypad(["ULL", "RRDDD", "LURDL", "UUUUD"])
        '5DB3'
    """
    code = ""
    position = 5
    for procedure in procedures:
        for instruction in procedure:
            match instruction, position:
                case ["D", (1 | 11)]:
                    position += 2
                case ["D", (2 | 3 | 4 | 6 | 7 | 8)]:
                    position += 4
                case ["U", (3 | 13)]:
                    position -= 2
                case ["U", (6 | 7 | 8 | 10 | 11 | 12)]:
                    position -= 4
                case ["L", (3 | 4 | 6 | 7 | 8 | 9 | 11 | 12)]:
                    position -= 1
                case ["R", (2 | 3 | 5 | 6 | 7 | 8 | 10 | 11)]:
                    position += 1
        code += format(position, "X")
    return code
