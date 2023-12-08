from parse import parse
from math import lcm

def preprocessing(input):
    directions, insts = input.split('\n\n')
    turn = {'R': {}, 'L': {}}
    for inst in insts.splitlines():
        (pos, left, right) = parse("{} = ({}, {})", inst)
        turn['L'][pos] = left
        turn['R'][pos] = right
    
    return list(directions), turn

def solver(directions, turn): 
    yield cnt_steps(directions, turn, 0)
    yield cnt_steps(directions, turn, 2)

def cnt_steps(directions, mapping, level):
    poss = [item for item in mapping['L'].keys() if item[- 3 + level:] == ('A' * (3 - level))]
    times = set()
    s = len(directions)
    for pos in poss:
        cnt = 0
        i = 0
        while pos[-3 + level:] != 'Z' * (3 - level):
            pos = mapping[directions[i]][pos]
            cnt += 1
            i = (i + 1) % s
        times.add(cnt)

    return lcm(*times)