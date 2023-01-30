from parse import parse

def generator(input): 
    return [list(parse('{:l} {:l} {:d} if {:l} {}', instruction)) for instruction in input.splitlines()]

def part_1(input): 
    return solver(input, 0)

def part_2(input):
    return solver(input, 1)


def solver(input, whole_process):
    reg, max_reg = {}, 0
    for r in list(set([p[0] for p in input])) : reg[r] = 0
    for ins in input:
        if eval(str(reg[ins[3]]) + ins[4]): reg[ins[0]] += (- 1 + 2 * (ins[1] == 'inc')) * ins[2]
        max_reg = max(max_reg, reg[ins[0]])
    return max([reg[item] for item in reg]+[whole_process * max_reg])
    