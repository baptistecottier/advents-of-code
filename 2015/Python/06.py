import itertools

def generator(input) :
    instructions = []
    for i in input.splitlines() :
        m = i.rsplit(' ',3)
        match m[0] :
            case "turn off" : instr = 0
            case "turn on" :instr = 1
            case "toggle" : instr = 2
        instructions.append([instr,[int(item) for item in m[1].split(',')],[int(item) for item in m[3].split(',')]])
    return instructions

def part_1(instructions) :
    return solver(instructions, 1)
    
def part_2(instructions) :
    return solver(instructions, 2)


def solver(instructions, part) :
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for [instr , [sx, sy], [ex, ey]] in instructions :
        points = list(itertools.product(range(sx, ex+1), range(sy, ey+1)))
        for (x,y) in points : 
            if instr !=4 - 2 * part : lights[x][y] = lights[x][y] * (part - 1) + instr 
            else : lights[x][y] = max(0, (-1) ** (part) * (lights[x][y] - 1))
    return sum([sum(lights[x]) for x in range(1000)])