from pythonfw.classes import Register

def preprocessing(input_):
    instructions = list()
    for instruction in input_.splitlines():
        data = instruction.split()
        match data[0]:
            case 'cpy': instructions.append((0, data[2], data[1]))
            case 'inc': instructions.append((1, data[1], 1))
            case 'dec': instructions.append((1, data[1], -1))
            case 'jnz': instructions.append((2, data[1], int(data[2])))
            case 'out': instructions.append((3, data[1], None))
    return instructions

def run(instructions, a):
    counter     = -1
    tictac      = 0 
    instruction = 0
    register    = Register(a, 0, 0, 0)

    while True:
        task, reg, val = instructions[instruction]
        match task: 
            case 0: 
                register[reg]  = register.get(val)
            case 1: 
                register[reg] += val
            case 2:
                if register.get(reg) != 0: instruction += val - 1
            case 3: 
                if tictac == register[reg]:
                    counter += 1
                    if counter > 10: return a
                    tictac   = 1 - tictac
                else: return 0
        instruction += 1

def solver(instructions):
    register_a = 0
    signal     = 0
    while signal == 0: 
        register_a += 1
        signal = run(instructions, register_a)
    yield signal