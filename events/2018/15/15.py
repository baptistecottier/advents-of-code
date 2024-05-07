from dataclasses import dataclass
from enum import Enum

@dataclass(unsafe_hash=True)
class Unit:
    team: str
    id: int
    x: int
    y: int
    hp: int 

def preprocessing(puzzle_input):
    area = list()
    id = 0
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c in "GE": area.append(Unit(c, id := id + 1, x, y, 200))
    return area

def solver(area):
    print(area)
    yield 1
#    while not (all(u.team == 'G' for u in area) or all(u.team == 'E' for u in area)):


