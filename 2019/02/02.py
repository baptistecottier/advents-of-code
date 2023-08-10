
from pythonfw.ship_computer import Program

def preprocessing(input: str) -> list[int]:
    return list(map(int, input.split(',')))

def solver(integers: list[int]):
    program: Program = Program(integers)
    program.run()
    delta = program.memory[0]
    
    program = Program([integers[0], 1, *integers[2:]])
    program.run()
    modulo = program.memory[0] - delta

    yield delta + 12 * modulo + 2
    
    target = 19_690_720 - delta
    yield target // modulo * 100 + (target % modulo)