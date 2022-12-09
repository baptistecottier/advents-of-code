import re
from json import loads
import builtins

def generator(input) : 
    return input

def part_1(input) :
    return solver(loads(input), 0)

def part_2(input) : 
    return solver(loads(input),1)

def solver(j ,reject_red):
    match type(j) :
        case builtins.int : return j
        case builtins.list : return sum([solver(j , reject_red) for j in j])
        case builtins.dict : return (reject_red or 'red' not in j.values()) * solver(list(j.values()), reject_red)
        case _: return 0
        