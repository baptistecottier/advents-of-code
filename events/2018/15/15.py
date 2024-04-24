from itertools import product


class Unit():
    def __init__(self, x, y, hp = 200) -> None:
        self.x = x
        self.y = y
        self.hp = hp
        self.damage = 3
        pass

def preprocessing(puzzle_input): 
    cave = set()
    elves = dict()
    gobelins = dict()
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            match c:
                case '#': cave.add((x, y))
                case 'E': elves.add(Unit(x, y))
                case 'G': gobelins.add(Unit(x, y))
            
    return cave, elves, gobelins

def solver(area):
    cave, elves, gobelins = area
    while elves and gobelins:
        for x, y in product(range(7), repeat=2):
            
    yield 1
    