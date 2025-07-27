"""
Advent of Code - Year 2015 - Day 1
https://adventofcode.com/2015/day/1
"""


def solver(instructions: str) -> tuple[int, int | None]:
    """
    Parse parenthesis instructions to track floor position.

    Args:
        instructions: A string of parenthesis where '(' means go up, ')' means go down.

    Returns:
        Tuple of (final floor number, position when basement is first entered or None)

    Raises:
        ValueError: If any character other than '(' or ')' is encountered.

    Examples:
        >>> solver("(())")
        (0, None)
        >>> solver("()()")
        (0, None)
        >>> solver("(((")
        (3, None)
        >>> solver("(()(()(")
        (3, None)
        >>> solver("))(((((")
        (3, 1)
        >>> solver("())")
        (-1, 3)
        >>> solver("))(")
        (-1, 1)
    """
    floor = 0
    basement = None

    for i, c in enumerate(instructions, 1):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        else:
            raise ValueError(f"Only parenthesis are accepted. Your instruction: {c}")

        if basement is None and floor < 0:
            basement = i

    return floor, basement
