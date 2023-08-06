def preprocessing(input_):
    return [list(map(int,program.split(' <-> ')[1].split(', '))) for program in input_.splitlines()]

def solver(input_):
    grps, sorted = [], []
    while len([item for sublist in grps for item in sublist]) != len(input_): 
        i = min(n for n in range(len(input_)) if n not in sorted)
        pipes = input_[i]
        grp = []
        while not all(x in grp for x in pipes):
            npipes = []
            for item in pipes:
                grp.append(item)
                npipes.extend(input_[item])
            pipes, grp, sorted = list(set(npipes)), list(set(grp)), list(set(sorted + pipes))
        grps.append(grp)
    yield len(grps[0])
    yield len(grps)

