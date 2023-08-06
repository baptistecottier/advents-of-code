from copy import deepcopy

def parser(input_):
    return [int(item) for item in input_.splitlines()]

def solver(offsets):
    yield steps_to_exit(deepcopy(offsets), lambda x: 1)
    yield steps_to_exit(offsets, lambda x: 1 if x < 3 else -1)
    
def steps_to_exit(offsets, func):
    steps   = 0
    pos     = 0
    
    while 0 <= pos < len(offsets):
        offsets[pos], pos = offsets[pos] + func(offsets[pos]), pos + offsets[pos]
        steps += 1
    return steps