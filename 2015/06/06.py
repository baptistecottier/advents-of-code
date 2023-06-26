import itertools

def parser(data):
    instructions = list()
    for instruction in data.splitlines():
        data = instruction.rsplit(' ',3)
        match data[0]:
            case "turn off": instr = 0
            case "turn on":  instr = 1
            case "toggle":   instr = 2
        instructions.append((instr, tuple(int(item) for item in data[1].split(',')), tuple(int(item) for item in data[3].split(','))))
    return instructions

def solver(instructions):
    def apply_instructions(func, trigger, coeff):
        lights = [[0 for _ in range(1000)] for _ in range(1000)]
        for instr , (sx, sy), (ex, ey) in instructions:
            for x in range(sx, ex + 1):
                for y in range(sy, ey + 1):
                    if instr == trigger: 
                        lights[x][y] = func(lights[x][y])
                    else: 
                        lights[x][y] = coeff * lights[x][y] + instr 
        return sum(sum(line) for line in lights) 
    
    yield apply_instructions(lambda x: 1 - x        , 2, 0)
    yield apply_instructions(lambda x: max(0, x - 1), 0, 1)