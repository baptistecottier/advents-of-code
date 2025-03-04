"""Advent of Code - Year 2015 - Day 01"""


def solver(instructions: str):
    """
    Solve puzzle by checking floor after each instruction. The first time a negative floor is met
    is stored as `basement` and yield for part 2, while the final floor is returned for part 1.
    
    Args: 
        instructions (str): Raw puzzle input
    
    Yields:
        1: The final floor
        2: Number of steps to reach the basement for the first time
    """
    floor = 0
    basement = None

    for i, c in enumerate(instructions, 1):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        else:
            raise ValueError(f"Only parenthesis are accepted. Your instruction: {c}")

        if basement is None and floor < 0:
            basement = i

    yield floor
    yield basement
