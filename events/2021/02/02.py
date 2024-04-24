def preprocessing(puzzle_input):
    commands = []
    for command in puzzle_input.splitlines():
        dir, steps = command.split(' ')
        match dir:
            case 'forward': commands.append((int(steps), 0          ))
            case 'up':      commands.append((0         , -int(steps)))
            case 'down':    commands.append((0         , int(steps) ))
    return commands

def solver(commands):
    x, y, y_aim, aim = 0, 0, 0, 0
    
    for dx, dy in commands:
        x     += dx
        y     += dy
        aim   += dy
        y_aim += dx * aim
        
    yield x * y
    yield x * y_aim