import re

def preprocessing(puzzle_input):
    game = list()
    for line in puzzle_input.splitlines():
        draws = [(int(n), "bgr".index(c)) for n, c in re.findall(r'([0-9]+)\s+(b|g|r)', line)]
        game.append(draws)
    return game

def solver(game):
    power = 0
    sumid = 0
    for id, draws in enumerate(game, 1): 
        if all(n + c < 15 for (n, c) in draws): sumid += id

        mb = max(n for (n, c) in draws if c == 0)
        mg = max(n for (n, c) in draws if c == 1)
        mr = max(n for (n, c) in draws if c == 2)
        power += mb * mg * mr

    yield sumid
    yield power