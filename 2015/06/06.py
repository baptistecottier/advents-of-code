import itertools

def generator(input):
    instructions = []
    for instruction in input.splitlines():
        data = instruction.rsplit(' ',3)
        match data[0]:
            case "turn off": instr = 0
            case "turn on":  instr = 1
            case "toggle":   instr = 2
        instructions.append([instr,[int(item) for item in data[1].split(',')],[int(item) for item in data[3].split(',')]])
    return instructions

def part_1(instructions):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for instr , (sx, sy), (ex, ey) in instructions:
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                if instr == 2: 
                    lights[x][y] ^= 1
                else: 
                    lights[x][y] = instr 
    return sum(sum(line) for line in lights)
    
def part_2(instructions):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for instr , (sx, sy), (ex, ey) in instructions:
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                if instr == 0: 
                    lights[x][y] = max(0, lights[x][y] - 1)
                else:
                    lights[x][y] += instr
    return sum(sum(line) for line in lights)