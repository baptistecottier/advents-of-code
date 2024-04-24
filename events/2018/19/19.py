from math import sqrt

def preprocessing(puzzle_input):
    instructions = list()
    lines = puzzle_input.splitlines()
    ip = int(lines.pop(0)[-1])
    for line in lines:
        details = line.split()
        a, b, c = list(int(n) for n in details[1:])
        instructions.append((details[0], a, b, c))
    return ip, instructions

def solver(*instructions):
    yield run(*instructions, 0)
    yield run(*instructions, 1)

def part_2(instructions):
    return run(*instructions, 1)

def run(ip, instructions, reg_zero):
    cycle = 1
    reg = [reg_zero, 0, 0, 0, 0, 0]
    while reg[5] == 0:
        op, a, b, c = instructions[reg[ip]]
        match op:
            case 'addr': reg[c] = reg[a] + reg[b]
            case 'addi': reg[c] = reg[a] + b
            case 'mulr': reg[c] = reg[a] * reg[b]
            case 'muli': reg[c] = reg[a] * b
            case 'gtrr': reg[c] = int(reg[a] > reg[b])
            case 'eqrr': reg[c] = int(reg[a] == reg[b])
            case 'setr': reg[c] = reg[a]
            case 'seti': reg[c] = a
            case _ : continue
        cycle += 1
        reg[ip] += 1
        if reg[ip] + 1 > len(instructions): return reg[0]
    return sum_divisors(reg[3])
   
def sum_divisors(n):
    divisors = set()
    for k in range(1, int(sqrt(n) + 1)):
        if n % k == 0 :
            divisors.add(k)
            divisors.add(n // k)
    return sum(divisors)