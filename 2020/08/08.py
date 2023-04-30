def generator(input):
    instructions = []
    for instruction in input.splitlines():
        ins, step = instruction.split(' ')
        instructions.append([ins, int(step)])
    return instructions

def part_1(input):
    return is_looping(input)[1]

from copy import deepcopy
def part_2(input): 
    modified_index = 0
    program = [['jmp', 0]]
    while is_looping(program)[0]:
        program = deepcopy(input)
        while input[modified_index][0] == 'acc': modified_index += 1
        program[modified_index][0] = ['nop', 'jmp'][input[modified_index][0] == 'nop']
        modified_index += 1
    return is_looping(program)[1]
        
        
def is_looping(program):
    i = 0 
    visited = []
    acc = 0
    while i in range(len(program)):
        if i in visited: 
            return (True, acc)
        else: 
            visited.append(i)
            ins, step = program[i]
            match ins:
                case 'acc': acc += step
                case 'jmp': i += step - 1
            i += 1
    return (False, acc)