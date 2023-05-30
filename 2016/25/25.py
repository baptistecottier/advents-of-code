def generator(input):
    instructions = list()
    for instruction in input.splitlines():
        data = instruction.split()
        match data[0]:
            case 'cpy': instructions.append((0, data[2], data[1]))
            case 'inc': instructions.append((1, data[1], 1))
            case 'dec': instructions.append((1, data[1], -1))
            case 'jnz': instructions.append((2, data[1], int(data[2])))
            case 'out': instructions.append((3, data[1], None))
    return instructions

def interpret(val,register):
    if val.isalpha(): 
         return register[val]
    return int(val)

def run(instructions, a):
    counter     = -1
    tictac      = 0 
    instruction = 0
    register    = {'a': a, 'b': 0, 'c': 0, 'd': 0}

    while(0 <= instruction < len(instructions)):
        task, reg, val = instructions[instruction]
        match task: 
            case 0: 
                register[reg]  = interpret(val, register)
            case 1: 
                register[reg] += val
            case 2:
                if interpret(reg, register) != 0: instruction += val - 1
            case 3: 
                if tictac == interpret(reg, register):
                    if (counter := counter + 1) > 10: return a
                    tictac   = 1 - tictac
                else: return 0
        instruction += 1

def part_1(instructions):
    register_a = 0
    signal     = 0
    while (signal := run(instructions, register_a)) == 0: 
        register_a += 1
    return signal

def part_2(instructions): 
    return "SIGNAL IS RETRASNMITTED"