"""
A module implementing an Intcode computer for Advent of Code 2019 puzzles.
"""

from collections import defaultdict
from collections.abc import Iterator
from copy import deepcopy


class Program(defaultdict):
    """
    A class that simulates an Intcode-like virtual machine with support for parameter modes, memory
    management, and input/output operations.
    """
    def __init__(self, intcode, phase=None):
        self.memory: defaultdict = defaultdict(int)
        for n, v in enumerate(intcode):
            self.memory[n] = v
        self.ptr: int = 0
        self.base: int = 0
        self.halt: bool = False
        self.phase: None | int = phase

    def get_memory(self):
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
            self.ptr += 1

    def run(self, *signal) -> int:
        """
        Executes the program loaded in memory, processing instructions and returning output or
        halting as specified by the opcodes.
        """
        signal = list(signal)
        while True:
            op = self.memory[self.ptr]
            self.ptr += 1
            match op % 100:
                case 1:
                    i_in1, i_in2, i_out = self.extract_indexes(op, 3)
                    self.memory[i_out] = self.memory[i_in1] + self.memory[i_in2]

                case 2:
                    i_in1, i_in2, i_out = self.extract_indexes(op, 3)
                    self.memory[i_out] = self.memory[i_in1] * self.memory[i_in2]

                case 3:
                    i_out, = self.extract_indexes(op, 1)
                    if self.phase is not None:
                        self.memory[i_out] = self.phase
                        self.phase = None
                    else:
                        self.memory[i_out] = signal.pop(0)

                case 4:
                    i_out, = self.extract_indexes(op, 1)
                    return self.memory[i_out]

                case 5:
                    i_in, i_out = self.extract_indexes(op, 2)
                    if self.memory[i_in] != 0:
                        self.ptr = self.memory[i_out]

                case 6:
                    i_in, i_out = self.extract_indexes(op, 2)
                    if self.memory[i_in] == 0:
                        self.ptr = self.memory[i_out]

                case 7:
                    i_in1, i_in2, i_out = self.extract_indexes(op, 3)
                    self.memory[i_out] = int(self.memory[i_in1] < self.memory[i_in2])

                case 8:
                    i_in1, i_in2, i_out = self.extract_indexes(op, 3)
                    self.memory[i_out] = int(self.memory[i_in1] == self.memory[i_in2])

                case 9:
                    i_out, = self.extract_indexes(op, 1)
                    self.base += self.memory[i_out]

                case 99:
                    self.halt = True
                    return -1
