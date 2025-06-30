"""Advent of Code - Year 2016 - Day 02"""

def preprocessing(puzzle_input: str) -> list[str]:
    """Process the input data by splitting it into lines.

    Parameters
    ----------
    data : str
        Raw input data as a single string

    Returns
    -------
    list[str]
        A list of strings where each element represents a line from the input data
    """
    return puzzle_input.splitlines()


def solver(procedure: list[str]):
    """
    Solves both parts of the Advent of Code 2016 Day 2 puzzle using different keypads.

    This function processes a list of movement instructions to find codes on two different
    keypad layouts: a squared (3x3) keypad and a diamond-shaped keypad.

    Args:
        procedure (list[str]): A list of strings where each string contains movement
            instructions using 'U' (up), 'D' (down), 'L' (left), and 'R' (right).

    Yields:
        str: First yield is the code obtained using the squared keypad (part 1)
        str: Second yield is the code obtained using the diamond keypad (part 2)
    """
    yield squared_keypad(procedure)
    yield diamond_keypad(procedure)


def squared_keypad(procedures: list[str]) -> str:
    """
    Computes the code for a standard 3x3 keypad based on a list of movement instructions.

    Each string in the `procedures` list represents a sequence of moves ('U', 'D', 'L', 'R') to be
    applied starting from the current position on the keypad. The keypad is arranged as follows:

        1 2 3
        4 5 6
        7 8 9

    The initial position is 5. For each procedure, the function processes the instructions and updates
    the position accordingly, ensuring moves that would go off the keypad are ignored. The resulting
    position after each procedure is appended to the code.

    Args:
        procedures (list[str]): A list of strings, each containing a sequence of movement instructions.

    Returns:
        str: The code formed by the final positions after processing each procedure.
    """
    code = ""
    position = 5
    for procedure in procedures:
        for instruction in procedure:
            match instruction, position:
                case ['D', (1| 2| 3| 4| 5| 6)]: position += 3
                case ['U', (4| 5| 6| 7| 8| 9)]: position -= 3
                case ['L', (2| 3| 5| 6| 8| 9)]: position -= 1
                case ['R', (1| 2| 4| 5| 7| 8)]: position += 1
        code += format(position)
    return code


def diamond_keypad(procedures: list[str]) -> str:
    """
    TONIGHT! I show you how to crack open a bathroom door code...
    Like a digital Indiana Jones, this function takes a list of procedures and decodes them into a
    glorious bathroom PIN.

    Using a diamond-shaped keypad that looks like this masterpiece:
        1
      2 3 4
    5 6 7 8 9
      A B C
        D

    And handling movements that would make a rally driver proud:
    - 'U': Goes Up (if possible)
    - 'D': Goes Down (if possible)
    - 'L': Goes Left (if possible)
    - 'R': Goes Right (if possible)

    Parameters:
    ----------
    procedures : list[str]
        A list of strings where each string contains the moves (U, D, L, R)
        Like a sophisticated GPS navigation system, but for your fingers

    Returns:
    -------
    str
        The most POWERFUL bathroom code you'll ever see
        Each digit represented in hexadecimal (0-9, A-D)
        And that's not just any code, that's the code that will get you in!

    And on that bombshell, let's crack on with it!
    """
    code = ""
    position = 5
    for procedure in procedures:
        for instruction in procedure:
            match instruction, position:
                case ['D', (1| 11)]:                    position += 2
                case ['D', (2| 3| 4| 6| 7| 8)]:         position += 4
                case ['U', (3| 13)]:                    position -= 2
                case ['U', (6| 7| 8| 10| 11| 12)]:      position -= 4
                case ['L', (3| 4| 6| 7| 8| 9| 11| 12)]: position -= 1
                case ['R', (2| 3| 5| 6| 7| 8| 10| 11)]: position += 1
        code += format(position, 'X')
    return code
