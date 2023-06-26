from parse    import parse
from operator import eq, lt, gt
from copy     import deepcopy

def parser(data: str): 
    aunts: dict = {}
    for aunt_data in data.splitlines():
        n, c1, v1, c2, v2, c3, v3 = parse("Sue {:d}: {}: {:d}, {}: {:d}, {}: {:d}", aunt_data)
        aunts[n] = {c1: v1, c2: v2, c3: v3}
    return aunts

def solver(aunts: dict):
    yield find_Sue(deepcopy(aunts), eq, eq)
    yield find_Sue(aunts, gt, lt)
        
def find_Sue(aunts: dict, op1, op2):
    Sue: dict = { "children": 3, "cats":     7, "samoyeds": 2, "pomeranians":  3, "akitas":   0, \
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