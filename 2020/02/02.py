from parse import parse

def generator(input): 
    return [parse("{:d}-{:d} {}: {}", pw)[:4] for pw in input.splitlines()]

def part_1(input):
    return sum([a <= pw.count(w) <= b for [a, b, w, pw] in input])

def part_2(input): 
    return sum([(pw[a-1] == w) ^ (pw[b-1] == w) for [a, b, w, pw] in input])
