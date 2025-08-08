# pylint: skip-file
# flake8: noqa
# type: ignore

"""
Advent of Code - Year 2023 - Day 19
https://adventofcode.com/2023/day/19
"""

from parse import parse
from itertools import product
def preprocessing(puzzle_input):
    wfs, ratings = puzzle_input.split('\n\n')
    workflows = dict()
    conds = dict()
    for wf in wfs.splitlines():
        w, cond = wf.split('{')
        conds[w] = list()
        cond = cond[:-1].split(',')
        for c in cond[:-1]:
            cc, th = c.split(':')
            conds[w].append((cc, th))
        conds[w].append(('True', cond[-1]))
    rr = set()
    for r in ratings.splitlines():
        (x, m, a, s) = parse("{x={:d},m={:d},a={:d},s={:d}}", r)
        rr.add((x, m, a, s))
    return rr, conds

def solver(rr, conds): 
    cnt = 0
    for x, m, a, s in rr:
        fw = 'in'
        while fw not in ['A', 'R']:
            for cd, th in conds[fw]:
                if eval(cd): 
                    fw = th
                    break
        if fw == 'A': cnt += x + m + a + s
    yield cnt

    for x in range(1, 4001):
        print(x)
        for m, a, s in product(range(1, 4001), repeat = 3):
            fw = 'in'
            while fw not in ['A', 'R']:
                for cd, th in conds[fw]:
                    if eval(cd): 
                        fw = th
                        break
            if fw == 'A': cnt += 1

    yield cnt

