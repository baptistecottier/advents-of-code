"""
Advent of Code - Year 2015 - Day 23
https://adventofcode.com/2015/day/23
"""

from collections.abc import Iterator


# Module-level functions to replace lambdas (required for multiprocessing pickling)
def _hlf(x: int) -> int:
    """Halve a number."""
    return x // 2


def _tpl(x: int) -> int:
    """Triple a number."""
    return x * 3


def _inc(x: int) -> int:
    """Increment a number."""
    return x + 1


def _jmp() -> int:
    """Jump instruction (always returns 1 for offset calculation)."""
    return 1


def _jie(x: int) -> int:
    """Jump if even (returns 1 if x is even, 0 if odd)."""
    return (1 + x) % 2


def _jio(x: int) -> int:
    """Jump if one (returns 1 if x == 1, else 0)."""
    return x == 1


def preprocessing(puzzle_input: str) -> list[tuple]:
    """
    Transform puzzle input into computer instructions.

    Turns assembly-like instructions into tuples with operation functions.

    Args:
        puzzle_input (str): Raw instructions

    Returns:
        list[tuple]: A list of instruction tuples (function, parameter)

    Example:
        >>> preprocessing("inc a\\njio a, +2\\ntpl a\\ninc a")
        [
            (_inc, 'a'),
            (_jio, (True, 1)),
            (_tpl, 'a'),
            (_inc, 'a')
        ]
    """
    ops = []
    for line in puzzle_input.splitlines():
        data = line.split(" ")
        match data[0]:
            case "hlf":
                ops.append((_hlf, data[1]))
            case "tpl":
                ops.append((_tpl, data[1]))
            case "inc":
                ops.append((_inc, data[1]))
            case "jmp":
                ops.append((_jmp, (False, int(data[1]) - 1)))
            case "jie":
                ops.append((_jie, (True, int(data[2]) - 1)))
            case "jio":
                ops.append((_jio, (True, int(data[2]) - 1)))
    return ops


def solver(lines: list[tuple]) -> Iterator[int]:
    """
    Executes a program with different initial values for register 'a' and yields the results.

    Args:
        lines: A list of instructions, each as a tuple containing a function and its arguments.

    Yields:
        int: The result of executing the program with 'a' initialized to 0 and then to 1.

    Example:
        results = list(solver(instructions))
        # results[0] is the output with a=0, results[1] with a=1
    """
    for a in [0, 1]:
        yield execute_program(lines, a)


def execute_program(lines: list[tuple], a: int) -> int:
    """
    Execute program with given instructions and initial 'a' value.

    Args:
        lines: List of instruction tuples (operation function, parameter)
        a: Initial value for register 'a'

    Returns:
        Final value of register 'b' after execution completes
    """
    reg = {"a": a, "b": 0}
    line = -1
    while (line := line + 1) < len(lines):
        f, arg = lines[line]
        if isinstance(arg, str):
            reg[arg] = f(reg[arg])
        else:
            test_a, n = arg
            if (test_a is False) or f(reg["a"]) != 0:
                line += n
    return reg["b"]

