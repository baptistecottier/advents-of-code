def preprocessing(input_):
    communications = []
    
    for communication in input_.splitlines():
        left = communication.split(' <-> ')[1]
        communications.append(list(map(int,left.split(', '))))

    return communications


def solver(communications):
    grps   = []
    sorted = []
    
    while len([item for sublist in grps for item in sublist]) != len(communications): 
        i = min(n for n in range(len(communications)) if n not in sorted)
        pipes = communications[i]
        grp = []
        while not all(x in grp for x in pipes):
            npipes = []
            for item in pipes:
                grp.append(item)
                npipes.extend(communications[item])
            pipes, grp, sorted = list(set(npipes)), list(set(grp)), list(set(sorted + pipes))
        grps.append(grp)

    yield len(grps[0])
    yield len(grps)

