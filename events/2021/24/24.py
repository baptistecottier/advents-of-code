from copy import deepcopy
from pythonfw.classes import Register

def preprocessing(puzzle_input):
    instructions = []
    blocks = puzzle_input.split('inp w\n')
    for block in blocks:
        block_instr = []
        block = block.splitlines()
        for inst in block:
            block_instr.append(inst.split(' '))
        instructions.append(block_instr)
    return instructions

def solver(instructions):
    model_number = 0
    temp_reg = Register({'w': 0, 'x': 0, 'y': 0, 'z': 0})
    for block in instructions:
        for w in range(9, 0, -1):
            reg = deepcopy(temp_reg)
            reg['w'] = w
            for op, dst, var in block:
                match op:
                    case 'add': reg[dst] += reg.get(var)
                    case 'mul': reg[dst] *= reg.get(var)
                    case 'div': reg[dst] //= reg.get(var)
                    case 'mod': reg[dst] %= reg.get(var)
                    case 'eql': reg[dst] = int(reg.get(var) == reg[dst])
                    case _: print(op)
            if reg['z'] == 0:
                model_number *= 10
                model_number += w
                temp_reg = deepcopy(reg)
                break
    yield model_number
                
                