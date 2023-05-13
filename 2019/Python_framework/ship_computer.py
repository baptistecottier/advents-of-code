from collections import defaultdict

class Program:
    def __init__(self):
        self.memory = defaultdict(int)
        self.ptr = 0
        self.base = 0
    
def generator(input):
    program = Program()
    for n, v in enumerate(input.split(',')):
        program.memory[n] = int(v)
    return program

def extract_indexes(op, program, nb_i):
    op //= 10
    indexes = []
    for _ in range(nb_i):
        match (op := op // 10) % 10:
            case 0: indexes.append(program.memory[program.ptr])
            case 1: indexes.append(program.ptr)
            case 2: indexes.append(program.base + program.memory[program.ptr])
        program.ptr += 1
    return tuple(indexes)
        
            
def run(program, inputs = []):
    outputs = []
    while True:
        op = program.memory[program.ptr]
        program.ptr += 1
        match op % 100:
            case 1: #addition
                i_in1, i_in2, i_out = extract_indexes(op, program, 3)
                program.memory[i_out] = program.memory[i_in1] + program.memory[i_in2]
                
            case 2: #multiplication
                i_in1, i_in2, i_out = extract_indexes(op, program, 3)
                program.memory[i_out] = program.memory[i_in1] * program.memory[i_in2]
                
            case 3: 
                i_out, = extract_indexes(op, program, 1)
                program.memory[i_out] = inputs.pop()
                
            case 4:
                i_out, = extract_indexes(op, program, 1)
                outputs.append(program.memory[i_out])

            case 5: 
                i_in, i_out = extract_indexes(op, program, 2)
                if program.memory[i_in] != 0: program.ptr = program.memory[i_out]
                
            case 6:
                i_in, i_out = extract_indexes(op, program, 2)
                if program.memory[i_in] == 0: program.ptr = program.memory[i_out]

            case 7: 
                i_in1, i_in2, i_out = extract_indexes(op, program, 3)
                program.memory[i_out] = int(program.memory[i_in1] < program.memory[i_in2])

            case 8: 
                i_in1, i_in2, i_out = extract_indexes(op, program, 3)
                program.memory[i_out] = int(program.memory[i_in1] == program.memory[i_in2])
            
            case 9: 
                i_out, = extract_indexes(op, program, 1)
                program.base += program.memory[i_out]
                
            case 99: 
                return outputs
            
            
