from collections import Counter

def generator(input):
    return  [''.join([message[i] for message in input.splitlines()]) for i in range(len(input.replace('\n','')) // input.count('\n'))]

def part_1(input) : 
    return solver(input, 0)

def part_2(input) : 
    return solver(input, -1)

def solver(input, order) :
    return ''.join([list((Counter(message).most_common()[order]))[0] for message in input]) 
