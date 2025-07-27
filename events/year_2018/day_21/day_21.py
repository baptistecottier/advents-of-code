"""
Advent of Code - Year 2018 - Day 21
https://adventofcode.com/2018/day/21
"""


def preprocessing(puzzle_input: str) -> tuple[int,
                                              list[tuple[str, int, int, int]],
                                              tuple[int, int]]:
    """
    Parses the puzzle input and extracts the instruction pointer, instructions, and the instruction
    involving register 0.

    Args:
        puzzle_input (str): The raw input string representing the instructions.

    Returns:
        tuple: (ip, instructions, inst_with_reg_0)
            ip (int): The instruction pointer index.
            instructions (list): List of instructions as tuples (op, a, b, c).
            inst_with_reg_0 (tuple): Tuple containing the line index and register index where
            register 0 is involved.
    """
    instructions = []
    lines = puzzle_input.splitlines()
    ip = int(lines.pop(0)[-1])
    inst_with_reg_0 = (-1, -1)

    for n, line in enumerate(lines):
        details = line.split()
        a, b, c = list(int(n) for n in details[1:])
        if 0 in [a, b] and 'r' in details[0]:
            inst_with_reg_0 = (n, a if b == 0 else b)
        instructions.append((details[0], a, b, c))

    if inst_with_reg_0 == (-1, -1):
        raise ValueError("At least one instruction must imply register 0")
    return ip, instructions, inst_with_reg_0


def solver(ip: int,
           instructions: list[tuple[str, int, int, int]],
           inst_with_reg_0: tuple[int, int]):
    """
    Simulates the program and yields values of the register involved with register 0 at the special
    instruction.

    Args:
        ip (int): The instruction pointer index.
        instructions (list): List of instructions as tuples (op, a, b, c).
        inst_with_reg_0 (tuple): Tuple containing the line index and register index where register
        0 is involved.

    Yields:
        int: The value of the register at the special instruction (first and last unique value
        before repetition).
    """
    line_inst_with_0, register_with_0 = inst_with_reg_0
    expected = None
    visited = set()
    reg = [0, 0, 0, 0, 0, 0]

    while True:
        op, a, b, c = instructions[reg[ip]]

        if reg[ip] == line_inst_with_0:
            if expected is None:
                yield reg[register_with_0]
            if reg[register_with_0] in visited:
                yield expected
                break
            expected = reg[register_with_0]
            visited.add(expected)

        match op:
            case 'addr': reg[c] = reg[a] + reg[b]
            case 'addi': reg[c] = reg[a] + b
            case 'mulr': reg[c] = reg[a] * reg[b]
            case 'muli': reg[c] = reg[a] * b
            case 'banr': reg[c] = reg[a] & reg[b]
            case 'bani': reg[c] = reg[a] & b
            case 'borr': reg[c] = reg[a] | reg[b]
            case 'bori': reg[c] = reg[a] | b
            case 'setr': reg[c] = reg[a]
            case 'seti': reg[c] = a
            case 'gtir': reg[c] = int(a > reg[b])
            case 'gtri': reg[c] = int(reg[a] > b)
            case 'gtrr': reg[c] = int(reg[a] > reg[b])
            case 'eqir': reg[c] = int(a == reg[b])
            case 'eqri': reg[c] = int(reg[a] == b)
            case 'eqrr': reg[c] = int(reg[a] == reg[b])
        reg[ip] += 1
