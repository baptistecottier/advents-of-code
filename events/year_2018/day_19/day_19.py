"""
Advent of Code - Year 2018 - Day 19
https://adventofcode.com/2018/day/19
"""

from collections.abc import Iterator
from math import sqrt


def preprocessing(puzzle_input: str) -> tuple[int, list[tuple[str, int, int, int]]]:
    """
    Parses the puzzle input and extracts the instruction pointer and instructions.

    Args:
        puzzle_input (str): The raw input string representing the instructions.

    Returns:
        Tuple[int, list[tuple[str, int, int, int]]]:
            The instruction pointer index and a list of instructions as tuples.
    """
    instructions = []
    lines = puzzle_input.splitlines()
    ip = int(lines.pop(0)[-1])
    for line in lines:
        details = line.split()
        a, b, c = list(int(n) for n in details[1:])
        instructions.append((details[0], a, b, c))
    return ip, instructions


def solver(ip: int, instructions: list[tuple[str, int, int, int]]) -> Iterator[int]:
    """
    Yields the results of running the instructions with register 0 set to 0 and 1.

    Args:
        ip (int): The instruction pointer index.
        instructions (list[tuple[str, int, int, int]]): The list of instructions.

    Yields:
        int: The result of the program for each initial value of register 0.
    """
    yield run(ip, instructions, 0)
    yield run(ip, instructions, 1)


def part_2(ip: int, instructions: list[tuple[str, int, int, int]]) -> int:
    """
    Runs the instructions with register 0 set to 1 and returns the result.

    Args:
        ip (int): The instruction pointer index.
        instructions (list[tuple[str, int, int, int]]): The list of instructions.

    Returns:
        int: The result of the program with register 0 set to 1.
    """
    return run(ip, instructions, 1)


def run(ip: int, instructions: list[tuple[str, int, int, int]], reg_zero: int) -> int:
    """
    Executes the instructions with the given initial value for register 0.

    Args:
        ip (int): The instruction pointer index.
        instructions (list[tuple[str, int, int, int]]): The list of instructions.
        reg_zero (int): The initial value for register 0.

    Returns:
        int: The result of the program or the sum of divisors of register 3.
    """
    cycle = 1
    reg = [reg_zero, 0, 0, 0, 0, 0]
    while reg[5] == 0:
        op, a, b, c = instructions[reg[ip]]
        match op:
            case 'addr': reg[c] = reg[a] + reg[b]
            case 'addi': reg[c] = reg[a] + b
            case 'mulr': reg[c] = reg[a] * reg[b]
            case 'muli': reg[c] = reg[a] * b
            case 'gtrr': reg[c] = int(reg[a] > reg[b])
            case 'eqrr': reg[c] = int(reg[a] == reg[b])
            case 'setr': reg[c] = reg[a]
            case 'seti': reg[c] = a
            case _: continue
        cycle += 1
        reg[ip] += 1
        if reg[ip] + 1 > len(instructions):
            return reg[0]
    return sum_divisors(reg[3])


def sum_divisors(n: int) -> int:
    """
    Calculates the sum of all divisors of a given integer.

    Args:
        n (int): The integer to find divisors for.

    Returns:
        int: The sum of all divisors of n.
    """
    divisors = set()
    for k in range(1, int(sqrt(n) + 1)):
        if n % k == 0:
            divisors.add(k)
            divisors.add(n // k)
    return sum(divisors)
