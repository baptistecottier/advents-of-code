from itertools              import product
from pythonfw.ship_computer import Program


def preprocessing(input_):
    return list(map(int, input_.split(',')))


def solver(intcode):
    beam = 0
    for tx, ty in product(range(50), repeat = 2):
        if Program(intcode).run(tx, ty): 
            beam += 1
            x, y = tx, ty
    yield beam

    while not Program(intcode).run(x - 99, y + 99):
        while Program(intcode).run(x, y): 
            x += 1
        y += 1
    yield 10_000 * (x - 100) + y - 1