def generator(input):
    return [list(map(int,program.split(' <-> ')[1].split(', '))) for program in input.splitlines()]

def part_1(input): return len(solver(input)[0])
    
def part_2(input): return len(solver(input))

def solver(input):
    grps, sorted = [], []
    while len([item for sublist in grps for item in sublist]) != len(input): 
        i = min([n for n in range(len(input)) if n not in sorted])
        pipes = input[i]
        grp = []
        while not all([x in grp for x in pipes]):
            npipes = []
            for item in pipes:
                grp.append(item)
                npipes.extend(input[item])
            pipes, grp, sorted = list(set(npipes)), list(set(grp)), list(set(sorted + pipes))
        grps.append(grp)
    return grps
