"""
Advent of Code - Year 2020 - Day 8
https://adventofcode.com/2020/day/8
"""


def preprocessing(puzzle_input: str) -> list[tuple[int, int]]:
    """
    Parses a string of instructions into a list of tuples, each containing an operation code and
    its argument.
    """
    instructions = []

    for instruction in puzzle_input.splitlines():
        ins, step = instruction.split(' ')
        match ins:
            case 'nop': instructions.append((0, int(step)))
            case 'acc': instructions.append((1, int(step)))
            case 'jmp': instructions.append((2, int(step)))

    return instructions


def solver(program: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Yields the accumulator value after running the program and after attempting to fix it by
    swapping a single 'jmp' and 'nop' instruction.
    """
    acc_value_after_first_repetition = test_program(program)[1]

    for i, prog in enumerate(program):
        ins, value = prog
        if ins == 1:
            continue
        program[i] = (2 - ins, value)
        code, acc = test_program(program)
        if code == "halt":
            return acc_value_after_first_repetition, acc
        program[i] = (ins, value)
    raise ValueError("Boot code could not be repaired")


def test_program(program: list[tuple[int, int]]) -> tuple[str, int]:
    """
    Simulates the execution of a program represented as a list of (instruction, value) tuples and
    returns a tuple indicating whether the program halts or loops, along with the accumulator value.
    """
    acc = 0
    index = 0
    visited = set()

    while True:
        if index in visited:
            return ("loop", acc)
        if index == len(program):
            return ("halt", acc)
        visited.add(index)
        ins, value = program[index]
        match ins:
            case 1:
                acc += value
            case 2:
                index += value - 1
        index += 1
