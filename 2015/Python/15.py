from parse import parse 
import math
def generator(input) : 
    return [parse("{}: capacity {:d}, durability {:d}, flavor {:d}, texture {:d}, calories {:d}",ingredient)[1:] for ingredient in input.splitlines()]

def part_1(input) : 
    return solver(input, False)

def part_2(input) :
    return solver(input, True) 


def solver(input, constraint):
    scores = [0,0]
    for i in range(100):
        a = [i * item for item in input[0]]
        for j in range(100-i):
            b = [j * item for item in input[1]]
            for k in range(100-(i+j)):
                l = 100 - (i+j+k) 
                c = [k * item for item in input[2]]
                d = [l * item for item in input[3]]
                score = math.prod([max(0,sum([v[index] for v in [a,b,c,d]])) for index in range(4)])
                scores[0] = max(scores[0], score)
                if sum([v[4] for v in [a,b,c,d]]) == 500 : scores[1] = max(scores[1], score)
    return scores[constraint]