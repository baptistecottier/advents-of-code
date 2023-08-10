import re

def preprocessing(input):
    lines = input.split('\n\n')
    draw  = [int(number) for number in lines[0].split(',')]
    grids = [[int(number) for number in re.findall(r'\d+', grid)] for grid in lines[1:]]
    grids = [[set(grid[5 * i: 5 * i + 5]) for i in range(5)] + [set(grid[i:: 5]) for i in range(5)] for grid in grids]
    return draw, grids 

def solver(game):
    yield first_win(game)
    yield last_lose(game)
    
    
def first_win(game): 
    draws, grids = game
    i = 5
    while i:= i+1:
        draw = set(draws[:i])
        for grid in grids: 
            if any(g < draw for g in grid): 
                return draws[i - 1] * sum(sum(g for g in gg if g not in draw) for gg in grid[:5])

def last_lose(game):
    draw, grids  = game
    while ball:= draw.pop():
        for grid in grids: 
            if all(not g < set(draw) for g in grid): 
                return ball * (sum(sum(g for g in gg if g not in draw) for gg in grid[:5]) - ball)