from itertools import *

def generator(input) : 
    return input 

def part_1(input) :
    return solver(input, 40)

def part_2(input):
    return solver(input, 50)

def solver(input, cycles):    
    for _ in range(cycles):
        input="".join([str(len(list(l))) + k for k , l in groupby(input)])
    return len(input)
    