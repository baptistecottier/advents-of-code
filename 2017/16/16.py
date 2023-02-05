def generator(input):
    dances = []
    
    for move in input.split(','):
        match move[0]:
            case 's': dance = (0,int(move[1:]))
            case 'x': dance = (1, sorted([int(item) for item in move[1:].split('/')]))
            case 'p': dance = (2, sorted(move[1:].split('/')))
        dances.append(dance)
    return dances

def part_1(input): 
    return solver(input, 'abcdefghijklmnop')

def part_2(input): 
    programs = solver(input, 'abcdefghijklmnop')
    cycle = 1
    while programs != 'abcdefghijklmnop': 
        programs = solver(input, programs)
        cycle += 1
    for _ in range(1_000_000_000 % cycle):
        programs = solver(input, programs)
    return programs


def solver(input, programs): 
    for dance, program in input:
        match dance:
            case 0: programs = programs[-program:]+programs[:-program]
            case 1: programs = programs[:program[0]]+programs[program[1]]+programs[program[0]+1:program[1]]+programs[program[0]]+programs[program[1]+1:]
            case 2: programs = programs.replace(program[0], '_').replace(program[1],program[0]).replace('_', program[1])
    return programs