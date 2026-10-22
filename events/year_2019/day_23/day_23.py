"""
Advent of Code - Year 2019 - Day 23
https://adventofcode.com/2019/day/23
"""

# Standard imports
from collections.abc import Iterator

# First party imports
from events.year_2019.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a comma-separated string of integers into a list of integers.
    """
    return list(map(int, puzzle_input.split(',')))


def solver(intcode: list[int]) -> Iterator[int]:
    """
    Simulates a network of 50 computers exchanging packets. Yields the Y value of the first packet
    sent to address 255, then the first Y value the NAT delivers to address 0 twice in a row.
    """
    programs = [Program(intcode, address) for address in range(50)]
    outputs: list[int] = []
    for address in range(50):
        outputs += collect_outputs(programs[address], -1)
    last_y = -1
    nat: list[int] = []

    while True:
        while outputs:
            new_outputs: list[int] = []
            while outputs:
                a, x, y = outputs.pop(0), outputs.pop(0), outputs.pop(0)
                if a == 255:
                    if not nat:
                        yield y
                    nat = [0, x, y]
                else:
                    new_outputs += collect_outputs(programs[a], x, y)
            outputs = new_outputs

        for address in range(50):
            outputs += collect_outputs(programs[address], -1)

        if not outputs:
            if not nat:
                raise ValueError("Wrong network configuration")
            if last_y == nat[2]:
                yield nat[2]
                return
            last_y = nat[2]
            outputs += nat


def collect_outputs(program: Program, *signal: int) -> list[int]:
    """
    Runs the program, passing the signal on the first call only, until it halts or waits for an
    input, and returns everything it output.
    """
    outputs: list[int] = []
    output = program.run(*signal)
    if output is not None:
        outputs.append(output)

    while (output := program.run()) is not None:
        outputs.append(output)
    return outputs
