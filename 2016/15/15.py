from math import prod
from AoC_tools import chinese_remainder
from parse import parse

def generator(input):
    a , n = [], []
    for disc in input.splitlines():
        d , tn , ta = parse('Disc #{:d} has {:d} positions; at time=0, it is at position {:d}.',disc)
        n.append(tn) 
        a.append(-(ta + d)) 
    return a, n

def part_1(input) : 
    a, n = input
    return chinese_remainder(n, a)

def part_2(input) : 
    a, n = input
    return chinese_remainder([prod(n),11], [chinese_remainder(n, a), -7] )
