from itertools          import product
from pythonfw.functions import extract_chunks


def preprocessing(input_):
    instructions  = []
    coordinates   = extract_chunks(input_, 4)

    for instruction in input_.splitlines():
        coord = coordinates.pop(0)
        if instruction.startswith("turn off"): 
            instructions.append((0, coord[:2], coord[2:]))
        elif instruction.startswith("turn on"):  
            instructions.append((1, coord[:2], coord[2:]))
        else:
            instructions.append((2, coord[:2], coord[2:]))

    return instructions


def solver(instructions):

    def apply_instructions(toggle, func, cumul):
        lights = [[0 for _ in range(1000)] for _ in range(1000)]
        
        for instr, (sx, sy), (ex, ey) in instructions:
            if instr == toggle: 
                for x, y in product(range(sx, ex + 1), range(sy, ey + 1)):
                    lights[x][y] = func(lights[x][y])
            else: 
                for x, y in product(range(sx, ex + 1), range(sy, ey + 1)):
                    lights[x][y] = lights[x][y] + instr if cumul else instr
                    
        return sum(sum(line) for line in lights) 

    yield apply_instructions(2, lambda x: 1 - x        , False)
    yield apply_instructions(0, lambda x: max(0, x - 1), True)