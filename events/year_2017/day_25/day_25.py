"""
Advent of Code - Year 2017 - Day 25
https://adventofcode.com/2017/day/25
"""

from parse import parse, Result


def preprocessing(puzzle_input: str) -> tuple[int, int, list[list[list[int]]]]:
    """
    Process the puzzle input to extract the starting state, diagnostic checkpoint trigger, and
    state transition details.

    Args:
        puzzle_input (str): The raw puzzle input containing the Turing machine instructions.

    Returns:
        tuple[int, int, list]: A tuple containing:
            - The starting state as an integer (A=0, B=1, etc.)
            - The number of steps before triggering the diagnostic checksum
            - A list of state transition details where each state has two conditions (0 or 1),
              each containing [write_value, move_left, next_state_index]

    Raises:
        ValueError: If the input format cannot be properly parsed.
    """
    infos = puzzle_input.split("\n\n")
    result = parse(
        "Begin in state {}.\nPerform a diagnostic checksum after {:d} steps.", infos[0]
    )
    if not isinstance(result, Result):
        raise ValueError("Invalid input format.")
    starting_state, trigger = result

    details = []
    for state in infos[1:]:
        result = parse(
            (
                """In state {}:\n  """
                """
    If the current value is 0:\n    """
                """
    - Write the value {:d}.\n    """
                """
    - Move one slot to the {}.\n    """
                """
    - Continue with state {}.\n  """
                """
    If the current value is 1:\n    """
                """
    - Write the value {:d}.\n    """
                """
    - Move one slot to the {}.\n    """
                """
    - Continue with state {}."""
            ),
            state,
        )

        if isinstance(result, Result):
            _, b, c, d, e, f, g = result
            details.append(
                [[b, c == "left", ord(d) - 65], [e, f == "left", ord(g) - 65]]
            )
    return ord(starting_state) - 65, trigger, details


def solver(state: int, trigger: int, details: list[list[list[int]]]) -> int:
    """
    Simulates a Turing machine with given state, steps, and transition details.

    Args:
        state: Initial state of the Turing machine.
        trigger: Number of steps to run the machine for.
        details: List of transition rules for each state.

    Yields:
        Sum of values on the tape after all steps.
    """
    tape = [0 for _ in range(trigger)]
    pos = 0
    for _ in range(trigger):
        infos = details[state]
        current_value = tape[pos]
        tape[pos] = infos[current_value][0]
        pos = pos + 1 - 2 * infos[current_value][1] % trigger
        state = infos[current_value][2]
    return sum(tape)
