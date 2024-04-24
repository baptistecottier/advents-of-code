from pythonfw.classes import Particule
from pythonfw.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]:
    return tuple(map(int, puzzle_input.split(',')))


def solver(*intcode):
    program  = Program(intcode)
    scaffold = set()
    x, y     = 0, 0
    while (output_ := program.run()) != None:
        match output_:
            case 10: x, y = -1, y + 1
            case 35: scaffold.add((x, y))
            case 46: pass
            case _ : robot = Particule(x, y, *{'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}[chr(output_)])
        x += 1

    intersections = {(x, y) for x, y in scaffold if all(neighbor in scaffold for neighbor in {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)})}
    yield sum(x * y for x, y in intersections)