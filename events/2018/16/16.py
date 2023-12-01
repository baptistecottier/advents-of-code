from copy               import deepcopy
from pythonfw.functions import extract_chunks

def preprocessing(input_):
    samples, tests = input_.split('\n\n\n\n')
    samples = [[sample[:4], sample[4:8], sample[8:]] for sample in extract_chunks(samples, 12)]
    tests   = extract_chunks(tests, 4)   
    return samples, tests

def solver(samples, tests): 
    good_samples   = 0
    matches        = {s: {c: 0 for c in range(16)} for s in range(16)}
    
    for before, instruction, after in samples:
        real_opcode  = instruction[0]
        good_opcodes = 0
        for opcode in range(16):
            instruction[0] = opcode
            if after == apply_opcode(instruction, deepcopy(before)):
                good_opcodes += 1
                matches[real_opcode][opcode] += 1
        if good_opcodes >= 3: good_samples += 1
    yield good_samples
    
    matches = {s: {c: n for c, n in matches[s].items() if n == max(matches[s].values())} for s in range(16)}
    perm    = dict()
    while len(perm) != 16:
        for opcode, candidates in matches.items():
            if len(candidates) == 1 : 
                perm_oc = candidates.popitem()[0]
                perm[perm_oc] = opcode
                del matches[opcode]
                for opcode, candidates in matches.items():
                    candidates.pop(perm_oc, None)
                break
            
    reg = [0, 0, 0, 0]
    for p in tests: reg = apply_opcode(p, reg, perm)
    yield reg[0]

def apply_opcode(instruction, reg, perm = {s: s for s in range(16)}):
    opcode, a, b, c = instruction
    if   opcode == perm.get(0):  reg[c] = reg[a] + reg[b]
    elif opcode == perm.get(1):  reg[c] = reg[a] + b
    elif opcode == perm.get(2):  reg[c] = reg[a] * reg[b]
    elif opcode == perm.get(3):  reg[c] = reg[a] * b
    elif opcode == perm.get(4):  reg[c] = reg[a] & reg[b]
    elif opcode == perm.get(5):  reg[c] = reg[a] & b
    elif opcode == perm.get(6):  reg[c] = reg[a] | reg[b]
    elif opcode == perm.get(7):  reg[c] = reg[a] | b
    elif opcode == perm.get(8):  reg[c] = reg[a]
    elif opcode == perm.get(9):  reg[c] = a
    elif opcode == perm.get(10): reg[c] = a > reg[b]
    elif opcode == perm.get(11): reg[c] = reg[a] > b
    elif opcode == perm.get(12): reg[c] = reg[a] > reg[b]
    elif opcode == perm.get(13): reg[c] = a == reg[b]
    elif opcode == perm.get(14): reg[c] = reg[a] == b
    elif opcode == perm.get(15): reg[c] = reg[a] == reg[b]
    return reg