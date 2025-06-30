"""Advent of Code - Year 2015 - Day 23"""

from collections.abc import Callable


def preprocessing(puzzle_input: str) -> list[tuple[int, Callable, str | int]]:
    """Transform puzzle input into computer instructions.
    
    Turns assembly-like instructions into tuples of pain and suffering.
    Warning: May cause uncontrollable urges to write more assembly code.

    Args:
        puzzle_input (str): Raw instructions that will ruin your day

    Returns:
        list[tuple]: A perfectly normal list of opcodes that definitely won't crash
    """
    ops = []
    for line in puzzle_input.splitlines():
        data = line.split(' ')
        match data[0]:
            case 'hlf':
                ops.append((lambda x: x // 2, data[1]))
            case 'tpl':
                ops.append((lambda x: x * 3, data[1]))
            case 'inc':
                ops.append((lambda x: x + 1, data[1]))
            case 'jmp':
                ops.append((lambda _: 1, (False, int(data[1]) - 1)))
            case 'jie':
                ops.append((lambda x: (1 + x) % 2, (True, int(data[2]) - 1)))
            case 'jio':
                ops.append((lambda x: x == 1, (True, int(data[2]) - 1)))
    return ops


def solver(lines: list[tuple[Callable, str | tuple[bool, int]]]):
    """Yields program execution results with registers initially set to 0 and 1 respectively."""
    yield execute_program(lines, 0)
    yield execute_program(lines, 1)


def execute_program(lines: list[tuple[Callable, str | tuple[bool, int]]], a: int) -> int:
    """Execute program with given instructions and initial 'a' value.
    
    Args:
        lines: List of instruction tuples (operation type, function, parameter)
        a: Initial value for register 'a'
        
    Returns:
        Final value of register 'b' after execution completes
    """
    reg = {"a": a , "b": 0}
    line = -1
    while (line := line + 1) < len(lines):
        f, arg = lines[line]
        if isinstance(arg, str):
            reg[arg] = f(reg[arg])

        else:
            test_a, n = arg
            if (test_a is False) or f(reg["a"]) != 0:
                line += n
    return reg['b']
