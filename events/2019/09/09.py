from pythonfw.ship_computer import Program

def preprocessing(puzzle_input): 
    return list(map(int, puzzle_input.split(',')))

def solver(intcodes): 
    yield Program(intcodes).run(1)
    yield Program(intcodes).run(2)