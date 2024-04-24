from math import sqrt

def preprocessing(puzzle_input):
    instructions = list()
    lines        = puzzle_input.splitlines()
    ip           = int(lines.pop(0)[-1])
    for line in lines:
        details = line.split()
        a, b, c = list(int(n) for n in details[1:])
        instructions.append((details[0], a, b, c))
    return ip, instructions


def solver(ip, instructions):
    m       = 0
    visited = set()
    reg     = [0, 0, 0, 0, 0, 0]
    while True:
        if tuple(reg) in visited: return reg
        else: visited.add(tuple(reg))
        op, a, b, c = instructions[reg[ip]]
        if reg[ip] ==  28:
            if m == 0:
                yield reg[4]
                break
            m = max(m, reg[4]) 
        match op:
            case 'addr': reg[c] = reg[a] + reg[b]
            case 'addi': reg[c] = reg[a] + b
            
            case 'mulr': reg[c] = reg[a] * reg[b]
            case 'muli': reg[c] = reg[a] * b
            
            case 'banr': reg[c] = reg[a] & reg[b]
            case 'bani': reg[c] = reg[a] & b
            
            case 'borr': reg[c] = reg[a] | reg[b]
            case 'bori': reg[c] = reg[a] | b
            
            case 'setr': reg[c] = reg[a]
            case 'seti': reg[c] = a
            
            case 'gtir': reg[c] = int(a > reg[b])
            case 'gtri': reg[c] = int(reg[a] > b)
            case 'gtrr': reg[c] = int(reg[a] > reg[b])
            
            case 'eqir': reg[c] = int(a == reg[b])
            case 'eqri': reg[c] = int(reg[a] == b)
            case 'eqrr': reg[c] = int(reg[a] == reg[b])
        reg[ip] += 1
   
def sum_divisors(n):
    divisors = set()
    for k in range(1, int(sqrt(n) + 1)):
        if n % k == 0 :
            divisors.add(k)
            divisors.add(n // k)
    return sum(divisors)