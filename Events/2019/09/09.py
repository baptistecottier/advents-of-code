from pythonfw.ship_computer import Program

def preprocessing(input): 
    return list(map(int, input.split(',')))

def solver(intcodes): 
    yield Program(intcodes).run(1)
    yield Program(intcodes).run(2)