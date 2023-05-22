def generator(input):
    return input.splitlines()

def part_1(lines): 
    return run_circuit(lines, 0)
        

def part_2(lines): 
    return run_circuit(lines, 1)

def run_circuit(lines, a):
    reg = {"a": a , "b": 0}
    i = 0
    while i < len(lines): 
        [ins , rem] = lines[i].split(' ', 1)
        match ins: 
            case 'hlf': reg[rem]/=2 
            case 'tpl': reg[rem]*=3 
            case 'inc': reg[rem]+=1 
            case 'jmp': i += int(rem)-1
            case 'jie': 
                [r, offset] = rem.split(', ', 1)
                if reg[r] % 2 == 0: i += int(offset) - 1
            case 'jio': 
                [r, offset] = rem.split(', ', 1)
                if reg[r]  == 1: i += int(offset) - 1
        i += 1
    return reg['b']