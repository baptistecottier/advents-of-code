import re
from json import loads
import builtins

def generator(input) : 
    return loads(input)

def part_1(input) :
    return solver(input, 1)

def part_2(input) : 
    return solver(input,0)

def solver(item ,allow_red):
    match type(item) :
        case builtins.int : return item
        case builtins.list : return sum([solver(subitem , allow_red) for subitem in item])
        case builtins.dict : return (allow_red or 'red' not in item.values()) * solver(list(item.values()), allow_red)
        case _: return 0
        