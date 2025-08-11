"""
Advent of Code - Year 2024 - Day 17
https://adventofcode.com/2024/day/17
"""

from collections import deque
from math import log


def preprocessing(puzzle_input: str) -> tuple[int, str]:
    """
    Preprocesses the puzzle input by extracting an integer and a formatted program string.
    """
    raw_regs, str_program = puzzle_input.split('\n\n')
    a = int(raw_regs.splitlines()[0].split()[-1])
    return a, str_program.replace(',', '').split(": ")[1]


def solver(a: int, str_program: str) -> tuple[str, int]:
    """
    Solves a puzzle by generating outputs and finding the minimum solution based on the given
    integer and program string.
    """
    program = [int(item) for item in str_program]
    param_a = program[3]
    final_outputs = ','.join(get_outputs(a, param_a))

    candidates = deque([str(k) for k in range(1, 8)])
    solutions = set()
    while candidates:
        candidate = candidates.popleft()
        for k in range(8):
            outputs = get_outputs(int(f"{candidate}{k}", 8), param_a)
            if outputs.startswith(str_program[-len(outputs):]):
                if len(outputs) == 16:
                    solutions.add(int(f"{candidate}{k}", 8))
                else:
                    candidates.append(f"{candidate}{k}")

    return final_outputs, min(solutions)


def bxor(a: int, b: int) -> int:
    """
    Returns the bitwise XOR of two integers, masked to 32 bits.
    """
    return int(a ^ b) & 0xffffffff


def getb(a: int, n: int, pa: int) -> int:
    """
    Computes and returns a transformed value based on the given integers a, n, and pa using bitwise
    operations.
    """
    a = a // pow(8, n - 1)
    b = bxor(a % 8, pa)
    c = a // pow(2, b)
    b = bxor(b, c)
    b = bxor(b, 7)
    return b % 8


def get_outputs(a: int, pa: int) -> str:
    """
    Returns a string concatenation of getb(a, k, pa) for k from 1 to log base 8 of a plus 1.
    """
    outputs = ""
    for k in range(1, int(log(a, 8)) + 2):
        outputs += str(getb(a, k, pa))
    return outputs
