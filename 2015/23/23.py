def generator(input):
    ops = []
    for line in input.splitlines():
        data = line.split(' ')
        match data[0]:
            case 'hlf': 
                ops.append((0, lambda x: x // 2, data[1]))
            case 'tpl': 
                ops.append((0, lambda x: x * 3, data[1]))
            case 'inc': 
                ops.append((0, lambda x: x + 1, data[1]))
            case 'jmp': 
                ops.append((1, lambda x: 1, int(data[1]) - 1))
            case 'jie': 
                ops.append((2, lambda x: (1 + x) % 2, int(data[2]) - 1))
            case 'jio': 
                ops.append((2, lambda x: x == 1, int(data[2]) - 1))
    return ops

def part_1(lines): 
    return execute_program(lines, 0)
        
def part_2(lines): 
    return execute_program(lines, 1)


def execute_program(lines, a):
    reg = {"a": a , "b": 0}
    line = -1
    while (line := line + 1) < len(lines): 
        v, f, n = lines[line]
        match v:
            case 0: reg[n] = f(reg[n])
            case 1: line += n
            case 2: 
                if f(reg["a"]): line += n
    return reg['b']