from pythonfw.functions import screen_reader


def preprocessing(puzzle_input): 
    instructions = []
    for instruction in puzzle_input.splitlines():
        instructions.append(0)
        if 'addx' in instruction: 
            instructions.append(int(instruction.split(' ')[1]))
    return instructions


def solver(instructions):
    x = 1
    strength = 0
    display = set()
    
    for i, shift in enumerate(instructions):
        if (i - 19) % 40 == 0: strength += (i + 1) * x
        if i % 40 in (x - 1, x, x + 1): display.add((i % 40, i // 40))
        x += shift
    
    yield strength
    yield screen_reader(display)
