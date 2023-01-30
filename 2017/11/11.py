def generator(input):
    return input.split(',')

def part_1(input):
    return solver(input)[-1]

def part_2(input):
    return max(solver(input))
    
def solver(input):
    visited = []
    x, y = 0, 0
    for step in input:
        x += (step in ['ne', 'se']) - (step in ['sw', 'nw'])
        y += (step in ['n', 'ne']) - (step in ['s', 'sw']) 
        visited.append(abs(x) + abs(y))
    return visited