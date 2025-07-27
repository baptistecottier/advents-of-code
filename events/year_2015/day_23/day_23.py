"""
Advent of Code - Year 2015 - Day 23
https://adventofcode.com/2015/day/23
"""

from collections.abc import Callable, Iterator


def preprocessing(puzzle_input: str) -> list[tuple[int, Callable, str | int]]:
    """
    Transform puzzle input into computer instructions.

    Turns assembly-like instructions into tuples of pain and suffering.
    Warning: May cause uncontrollable urges to write more assembly code.

    Args:
        puzzle_input (str): Raw instructions that will ruin your day

    Returns:
        list[tuple]: A perfectly normal list of opcodes that definitely won't crash

    Example:
        >>> preprocessing("inc a\njio a, +2\ntpl a\ninc a")
        [
            (<function ...>, 'a'),
            (<function ...>, (True, 1)),
            (<function ...>, 'a'),
            (<function ...>, 'a')
        ]
    """
    ops = []
    for line in puzzle_input.splitlines():
        data = line.split(" ")
        match data[0]:
            case "hlf":
                ops.append((lambda x: x // 2, data[1]))
            case "tpl":
                ops.append((lambda x: x * 3, data[1]))
            case "inc":
                ops.append((lambda x: x + 1, data[1]))
            case "jmp":
                ops.append((lambda: 1, (False, int(data[1]) - 1)))
            case "jie":
                ops.append((lambda x: (1 + x) % 2, (True, int(data[2]) - 1)))
            case "jio":
                ops.append((lambda x: x == 1, (True, int(data[2]) - 1)))
    return ops


def solver(lines: list[tuple[Callable, str | tuple[bool, int]]]) -> Iterator[int]:
    """
    Executes a program with different initial values for register 'a' and yields the results.

    Args:
        lines (list[tuple[Callable, str | tuple[bool, int]]]):
            A list of instructions, each as a tuple containing a callable and its arguments.

    Yields:
        int: The result of executing the program with 'a' initialized to 0 and then to 1.

    Example:
        results = list(solver(instructions))
        # results[0] is the output with a=0, results[1] with a=1
    """
    for a in [0, 1]:
        yield execute_program(lines, a)


def execute_program(
    lines: list[tuple[Callable, str | tuple[bool, int]]], a: int
) -> int:
    """
    Execute program with given instructions and initial 'a' value.

    Args:
        lines: List of instruction tuples (operation type, function, parameter)
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
