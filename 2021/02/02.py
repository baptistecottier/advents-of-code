def generator(input):
    commands = []
    for command in input.splitlines():
        dir, steps = command.split(' ')
        match dir:
            case 'forward': commands.append((int(steps), 0))
            case 'up': commands.append((0, - int(steps)))
            case 'down': commands.append((0, int(steps)))
    return commands

def part_1(input): 
    return solver(input, False)

def part_2(input): 
    return solver(input, True)

def solver(commands, track_aim):
    x, y, aim = 0, 0, 0
    for dx, dy in commands:
        x += dx
        aim += dy
        y += [dy, dx * aim][track_aim]
    return x * y