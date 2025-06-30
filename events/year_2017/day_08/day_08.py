"""Advent of Code - Year 2017 - Day 08"""

import operator
from dataclasses import dataclass
from collections.abc import Callable, Generator

@dataclass
class Instruction:
    """
    A class representing an instruction for register manipulation.
    Attributes:
        reg_a (str): The target register to be modified.
        coeff (int): The coefficient to be applied to the operation.
        reg_b (str): The reference register used in the condition.
        f (callable): The condition function to be evaluated.
        value (int): The value to compare against in the condition.
    """
    reg_a: str
    coeff: int
    reg_b: str
    f: Callable
    value: int


def preprocessing(puzzle_input: str) -> list[Instruction]:
    """
    Convert puzzle input into a list of instruction objects.
    
    Maps comparison operators from strings to functions and parses each line into an
    Instruction object, adjusting coefficients for 'dec' operations.
    
    Args:
        puzzle_input: String containing the puzzle input with instructions
        
    Returns:
        List of Instruction objects
    """
    str_to_op ={
        '==': operator.eq,
        '!=': operator.ne,
        '<' : operator.lt,
        '<=': operator.le,
        '>' : operator.gt,
        '>=': operator.ge,
    }
    instructions = []
    for instruction in puzzle_input.splitlines():
        data = instruction.split()
        coeff = int(data[2])
        if data[1] == 'dec':
            coeff *= -1
        instructions.append(Instruction(data[0], coeff, data[4], str_to_op[data[5]], int(data[6])))
    return instructions


def solver(instructions: list[Instruction]) -> Generator[int, None, None]:
    """
    Executes a list of register instructions and yields the maximum register values.
    
    The function processes each instruction, updating registers based on conditional checks.
    It tracks both the final maximum register value and the highest value ever reached.
    
    Args:
        instructions: List of Instruction objects containing register operations and conditions
        
    Yields:
        int: Maximum register value at the end of execution
        int: Maximum register value observed during the entire execution
    """
    max_reg   = 0
    registers = {v.reg_a: 0 for v in instructions}

    for instr in instructions:
        if instr.f(registers[instr.reg_b], instr.value):
            registers[instr.reg_a] += instr.coeff
            max_reg = max(max_reg, registers[instr.reg_a])

    yield max(registers.values())
    yield max_reg
