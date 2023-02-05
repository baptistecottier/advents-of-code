from parse import parse
from itertools import chain

def generator(input):
    details = []
    for p in input.splitlines():
        match len(p.split(' -> ')):
            case 1: details.append(list(parse("{} ({:d})",p)))
            case 2: details.append(list(parse("{} ({:d}) -> {}", p))[:-1] + list(parse("{} ({:d}) -> {}", p))[-1].split(', '))
    return details

def part_1(input): return [item for item in [p[0] for p in input] if item not in chain(*[p[2:] for p in input])][0]

def part_2(input):
    w = {}
    for program in [p[0] for p in input]: w[program] = weight(input, program)
    pp = min([program[2:] for program in [item for item in input if len(item) > 2] if not all(w[p] == w[program[2:][0]] for p in program[2:])], key = lambda x: sum([w[item] for item in x]))
    return input[[p[0] for p in input].index([x for x in pp if sum([w[x] == w[xx] for xx in pp])==1][0])][1] + min([w[x] for x in pp]) - max([w[x] for x in pp])


def weight(input, program): return input[[p[0] for p in input].index(program)][1] + sum([weight(input, item) for item in input[[p[0] for p in input].index(program)][2:]])
