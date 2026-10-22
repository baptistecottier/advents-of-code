"""
A module implementing an Intcode computer for Advent of Code 2019 puzzles.
"""

from collections import defaultdict
from collections.abc import Callable, Iterable, Iterator
from copy import deepcopy
from operator import add, mul


BINARY_OPS: dict[int, Callable[[int, int], int]] = {
    1: add,
    2: mul,
    7: lambda a, b: int(a < b),
    8: lambda a, b: int(a == b),
}


class Program:
    """
    A class that simulates an Intcode-like virtual machine with support for parameter modes, memory
    management, and input/output operations.
    """
    def __init__(self, intcode: Iterable[int], inputs: int | list[int] | None = None):
        self.memory: defaultdict[int, int] = defaultdict(int)
        for n, v in enumerate(intcode):
            self.memory[n] = v
        self.ptr: int = 0
        self.base: int = 0
        self.halt: bool = False
        if isinstance(inputs, int):
            inputs = [inputs]
        self.inputs: None | list[int] = inputs

    def get_memory(self) -> tuple[int, ...]:
        """
        Returns a deep copy of the current memory values as a tuple.
        """
        return deepcopy(tuple(self.memory.values()))

    def extract_indexes(self, opcode: int, nb_i: int) -> Iterator[int]:
        """
        Extracts a list of memory indexes based on the parameter modes encoded in the given opcode
        for a specified number of parameters.
        """
        opcode //= 10
        for _ in range(nb_i):
            match (opcode := opcode // 10) % 10:
                case 0:
                    yield self.memory[self.ptr]
                case 1:
                    yield self.ptr
                case 2:
                    yield self.base + self.memory[self.ptr]
                case mode:
                    raise ValueError(f"Unknown parameter mode {mode}")
            self.ptr += 1

    def next_input(self, signals: list[int]) -> int | None:
        """
        Pops the next input, taken from the inputs given at creation first, then from the signals
        given to run. Returns None when there is none left.
        """
        if self.inputs is not None:
            value = self.inputs.pop(0)
            if self.inputs == []:
                self.inputs = None
            return value
        if signals:
            return signals.pop(0)
        return None

    def run(self, *signal: int) -> int | None:
        """
        Executes the program loaded in memory, processing instructions and returning output or
        halting as specified by the opcodes.
        """
        signals = list(signal)
        while True:
            op = self.memory[self.ptr]
            self.ptr += 1
            match op % 100:
                case code if code in BINARY_OPS:
                    i_in1, i_in2, i_out = self.extract_indexes(op, 3)
                    self.memory[i_out] = BINARY_OPS[code](self.memory[i_in1], self.memory[i_in2])

                case 3:
                    i_out, = self.extract_indexes(op, 1)
                    if (value := self.next_input(signals)) is None:
                        # Waits for an input: point back to this instruction to read it next run
                        self.ptr -= 2
                        return None
                    self.memory[i_out] = value

                case 4:
                    i_out, = self.extract_indexes(op, 1)
                    return self.memory[i_out]

                case 5 | 6 as code:
                    i_in, i_out = self.extract_indexes(op, 2)
                    # 5 jumps if the value is non-zero, 6 if it is zero
                    if (self.memory[i_in] != 0) == (code == 5):
                        self.ptr = self.memory[i_out]

                case 9:
                    i_out, = self.extract_indexes(op, 1)
                    self.base += self.memory[i_out]

                case 99:
                    self.halt = True
                    return None

                case code:
                    raise ValueError(f"Unknown opcode {code}")
