from parse import parse
from operator import eq, lt, gt

def generator(input): 
    aunts = {}
    for aunt_data in input.splitlines():
        n, c1, v1, c2, v2, c3, v3 = parse("Sue {:d}: {}: {:d}, {}: {:d}, {}: {:d}", aunt_data)
        aunts[n] = {c1: v1, c2: v2, c3: v3}
    return aunts

def part_1(aunts): 
    return find_Sue(aunts, eq, eq)

def part_2(aunts): 
    return find_Sue(aunts, gt, lt)
        
def find_Sue(aunts, op1, op2):
    Sue = { "children": 3, "cats":     7, "samoyeds": 2, "pomeranians":  3, "akitas":   0, \
            "vizslas":  0, "goldfish": 5, "trees":    3, "cars":         2, "perfumes": 1}
    
    for n, compounds in aunts.items():
        for compound, value in list(compounds.items()):
            if compound in ['cats', 'trees']:
                if op1(value, Sue[compound]): del aunts[n][compound]
                else: break
            elif compound in ['pomeranians', 'goldfish']:
                if op2(value, Sue[compound]): del aunts[n][compound]
                else: break
            elif value == Sue[compound]: del aunts[n][compound]
        if compounds == {}: return n