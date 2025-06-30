"""Advent of Code - Year 2017 - Day 16"""

def preprocessing(puzzle_input: str) -> list[tuple]:
    """Process the puzzle input to create a list of dance moves.

    The function takes a string of comma-separated dance moves and converts them into a structured
    format. Each move is converted into a tuple containing:
    - Move type (0 for spin 's', 1 for exchange 'x', 2 for partner 'p')
    - Values associated with the move

    Parameters:
        puzzle_input (str): A string of comma-separated dance moves

    Returns:
        list: A list of tuples, each containing:
            - int: Move type identifier (0, 1, or 2)
            - For spin ('s'): int representing number of positions
            - For exchange ('x'): list of two sorted integers representing positions
            - For partner ('p'): sorted list of two program names

    Example:
        >>> preprocessing('s1,x3/4,pa/b')
        [(0, 1), (1, [3, 4]), (2, ['a', 'b'])]
    """
    dances = []
    for move in puzzle_input.split(','):
        match move[0]:
            case 's':
                value = int(move[1:])
                dance = (0, [value])
            case 'x':
                values = sorted([int(item) for item in move[1:].split('/')])
                dance = (1, values)
            case 'p':
                dance = (2, sorted(move[1:].split('/')))
            case _:
                raise ValueError(f"Incorrect dance move: {move}")
        dances.append(dance)
    return dances


def solver(dance: list[tuple]):
    """Solve dance program sequence puzzle.

    This function takes a series of dance moves and determines the final position
    of programs after performing the dance sequence. It handles both part 1 (single dance)
    and part 2 (1 billion dances) by detecting cycles in the sequence.

    Args:
        dance (list): List of dance move instructions

    Yields:
        str: Two strings are yielded:
            1. The program order after one dance
            2. The program order after 1 billion dances, calculated using cycle detection

    Note:
        - Programs start in order 'a' through 'p'
        - Dance moves can include spins, exchanges, and partner swaps
        - Function detects when sequence starts repeating to efficiently calculate
          the result after 1 billion iterations
    """
    programs = list('abcdefghijklmnop')
    orders = []
    orders.append(order_program(dance, programs.copy()))
    yield "".join(orders[0])

    cycle = 1
    while orders[-1] != programs:
        orders.append(order_program(dance, orders[-1].copy()))
        cycle += 1
    yield "".join(orders[1_000_000_000 % cycle - 1])


def order_program(dances: list[tuple], programs: list[str]) -> list[str]:
    """
    Rearranges programs according to a list of dance moves.
    
    Args:
        dances: List of dance moves, each represented as a tuple (dance_type, data).
               Dance types:
               - 0: Spin (data[0] is the number of positions)
               - 1: Exchange (data[0] and data[1] are positions to swap)
               - 2: Partner (data[0] and data[1] are program names to swap)
        programs: List of program names to be rearranged.
    
    Returns:
        A new arrangement of the programs after performing all dance moves.
    """
    for dance, data in dances:
        match dance:
            case 0:
                programs = programs[-data[0]:] + programs[:-data[0]]
            case 1:
                programs[data[0]], programs[data[1]] = programs[data[1]], programs[data[0]]
            case 2:
                for i, p in enumerate(programs):
                    if p == data[0]:
                        programs[i] = data[1]
                    elif p == data[1]:
                        programs[i] = data[0]
    return programs
