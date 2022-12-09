from parse import *

def generator(input) : 
    [a, b] = input.split('\n\n')
    rearrangements = []
    for r in b.splitlines() :
        rearrangements.append(parse("move {:d} from {:d} to {:d}", r)[:3])
    
    cargo_lines = a.splitlines()
    cargo_width = len(cargo_lines[-1].replace(' ',''))
    cargo = ["" for _ in range(cargo_width)]
    for c in cargo_lines[:-1] : 
        v = c.split('[')
        s = len(v[0]) // 4
        for cc in v[1:] :
            cargo[s] =  cc[0] + cargo[s]
            s += 1 + (cc.count(' ') // 4)
    return (cargo, rearrangements)

def part_1(input) :
    return solver(input, -1)

def part_2(input) :
    return solver(input, 1)

def solver(input, version) : 
    (cargo , rearrangements) = input
    cargo = list(cargo)
    for (l, s, e) in rearrangements :
        cargo[e-1] += cargo[s-1][-l:][::version]
        cargo[s-1] = cargo[s-1][:-l]
    return ''.join([c[-1] for c in cargo])