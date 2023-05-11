import re

def generator(input):
    lines = input.split('\n\n')
    draw = [int(number) for number in lines[0].split(',')]
    grids = [[int(number) for number in re.findall(r'\d+', grid)] for grid in lines[1:]]
    grids = [[set(grid[5 * i : 5 * i + 5]) for i in range(5)] + [set(grid[i :: 5]) for i in range(5)] for grid in grids]
    return draw, grids 

def part_1(input): 
    draws, grids = input
    i = 5
    while i := i+1:
        draw = set(draws[:i])
        for grid in grids: 
            if any(g < draw for g in grid) : 
                return input[0][i - 1] * sum(sum(g for g in gg if g not in draw) for gg in grid[:5])

def part_2(input):
    draw, grids  = input
    while ball := draw.pop():
        for grid in grids: 
            if all(not g < set(draw) for g in grid) : 
                return ball * (sum(sum(g for g in gg if g not in draw) for gg in grid[:5]) - ball)