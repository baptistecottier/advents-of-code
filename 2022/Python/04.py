from parse import * 

def generator(input) :
    return [[int(n) for n in parse("{}-{},{}-{}", line)[:4]] for line in input.splitlines()]

def part_1(input):
    return solver(input)
    
def part_2(input) :
    return solver([[a ,b, d, c] for [a, b, c, d] in input])

def solver(input) :
    return sum([(a - c) * (b - d) <= 0 for [a,b,c,d] in input])
