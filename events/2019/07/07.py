from itertools              import permutations
from pythonfw.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]: 
    return list(map(int, puzzle_input.split(',')))


def solver(intcode):
    highest = 0
    for setting in permutations([0, 1, 2, 3, 4]):
        signal = 0
        for phase in setting:
            program = Program(intcode, phase)
            signal = program.run(signal)
        if signal > highest: highest = signal
    yield highest
    
    highest = 0
    for setting in permutations([5, 6, 7, 8, 9]):
        signal = 0
        last_signal = None
        programs = [Program(intcode, phase) for phase in setting]
        while not any([program.halt for program in programs]):
            for program in programs:
                signal = program.run(signal)
                if signal:
                    last_signal = signal
        if last_signal > highest: highest = last_signal
    yield highest