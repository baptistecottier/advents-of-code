"""
Advent of Code - Year 2017 - Day 16
https://adventofcode.com/2017/day/16
"""


def preprocessing(puzzle_input: str) -> list[tuple]:
    """
    Process puzzle input into structured dance moves.

    Args:
        puzzle_input (str): Comma-separated dance moves

    Returns:
        list[tuple]: List of (move_type, values) tuples where:
            - 0: spin, values=[positions]
            - 1: exchange, values=[pos1, pos2]
            - 2: partner, values=[name1, name2]
    """
    dances = []
    for move in puzzle_input.split(","):
        match move[0]:
            case "s":
                value = int(move[1:])
                dance = (0, [value])
            case "x":
                values = sorted([int(item) for item in move[1:].split("/")])
                dance = (1, values)
            case "p":
                dance = (2, sorted(move[1:].split("/")))
            case _:
                raise ValueError(f"Incorrect dance move: {move}")
        dances.append(dance)
    return dances


def solver(dance: list[tuple]) -> tuple[str, str]:
    """
    Solve dance program sequence puzzle.

    This function takes a series of dance moves and determines the final position
    of programs after performing the dance sequence. It handles both part 1 (single dance)
    and part 2 (1 billion dances) by detecting cycles in the sequence.

    Args:
        dance (list): List of dance move instructions

    Yields:
        str: Two strings are yielded:
            1. The program order after one dance
            2. The program order after 1 billion dances, calculated using cycle detection
    """
    programs = list("abcdefghijklmnop")
    orders = []
    orders.append(order_program(dance, programs.copy()))
    cycle = 1

    while orders[-1] != programs:
        orders.append(order_program(dance, orders[-1].copy()))
        cycle += 1
    return "".join(orders[0]), "".join(orders[1_000_000_000 % cycle - 1])


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
                programs = programs[-data[0]:] + programs[: -data[0]]
            case 1:
                programs[data[0]], programs[data[1]] = (
                    programs[data[1]],
                    programs[data[0]],
                )
            case 2:
                for i, p in enumerate(programs):
                    if p == data[0]:
                        programs[i] = data[1]
                    elif p == data[1]:
                        programs[i] = data[0]
    return programs
