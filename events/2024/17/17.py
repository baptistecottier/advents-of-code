from collections import deque
from math        import log


def preprocessing(puzzle_input):
    raw_regs, raw_program = puzzle_input.split('\n\n')
    a = int(raw_regs.splitlines()[0].split()[-1])
    program = raw_program.replace(',','')
    return a, program


def solver(a, program):
    yield ','.join(get_outputs(a))
    
    # We know a need to be greater than 2^15 so k > 0
    candidates = deque([str(k) for k in range(1, 8)]) 
    solutions = set()
    while candidates:
        candidate = candidates.popleft()
        for k in range(8): 
            outputs = get_outputs(int(f"{candidate}{k}", 8))
            if outputs.startswith(program[-len(outputs):]):
                if len(outputs) == 16:
                    solutions.add(int(f"{candidate}{k}", 8))
                else: candidates.append(f"{candidate}{k}")
    yield min(solutions)


def bxor(a, b):
    return int(a ^ b) & 0xffffffff

def getb(a, n = 1):
    a = a // pow(8, n - 1)
    b = bxor(a % 8, 2)
    c = a // pow(2, b)

    b = bxor(b, 7)
    b = bxor(b, c)
    return (b % 8)

def get_outputs(a):
    outputs = ""
    for k in range(1, int(log(a, 8)) + 2):
        outputs += str(getb(a, k))
    return outputs    