from collections import defaultdict
from copy import deepcopy

class Program(defaultdict):
    def __init__(self, intcode, phase = None):
        self.memory: defaultdict = defaultdict(int)
        for n, v in enumerate(intcode):
            self.memory[n] = v
        self.ptr:  int  = 0
        self.base: int  = 0
        self.halt: bool = False
        self.phase: int = phase
    
    def get_memory(self):
        return deepcopy(tuple(self.memory.values()))

    def extract_indexes(self, opcode: int, nb_i: int):
        opcode //= 10
        indexes: list[int] = []
        for _ in range(nb_i):
            match (opcode:= opcode // 10) % 10:
                case 0: indexes.append(self.memory[self.ptr])
                case 1: indexes.append(self.ptr)
                case 2: indexes.append(self.base + self.memory[self.ptr])
            self.ptr += 1
        return indexes
        
    def run(self, signal = None):
        while True:
            op = self.memory[self.ptr]
            self.ptr += 1
            match op % 100:
                case 1: #addition
                    i_in1, i_in2, i_out = self.extract_indexes(op, 3)
                    self.memory[i_out] = self.memory[i_in1] + self.memory[i_in2]
                    
                case 2: #multiplication
                    i_in1, i_in2, i_out = self.extract_indexes(op, 3)
                    self.memory[i_out] = self.memory[i_in1] * self.memory[i_in2]
                    
                case 3: 
                    i_out, = self.extract_indexes(op, 1)
                    if self.phase != None:
                        self.memory[i_out] = self.phase
                        self.phase = None
                    else: self.memory[i_out] = signal
                    
                case 4:
                    i_out, = self.extract_indexes(op, 1)
                    return self.memory[i_out]

                case 5: 
                    i_in, i_out = self.extract_indexes(op, 2)
                    if self.memory[i_in] != 0: self.ptr = self.memory[i_out]
                    
                case 6:
                    i_in, i_out = self.extract_indexes(op, 2)
                    if self.memory[i_in] == 0: self.ptr = self.memory[i_out]

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
                    return None
                
                
