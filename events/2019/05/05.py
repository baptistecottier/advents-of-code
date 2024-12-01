from pythonfw.ship_computer import Program 


def preprocessing(puzzle_input: str) -> list[int]: 
    return list(map(int, puzzle_input.split(',')))


def solver(integers: list[int]):
    TEST = Program(integers)
    while True:
        output = TEST.run(1)
        if (output == None) or (output != 0): 
            break
    yield output
    yield Program(integers).run(5)

