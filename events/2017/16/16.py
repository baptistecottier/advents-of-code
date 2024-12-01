def preprocessing(input_):
    dances = []
    n_programs = 0
    for move in input_.split(','):
        match move[0]:
            case 's': 
                value = int(move[1:])
                dance = (0, value)
                n_programs = max(n_programs, value)
            case 'x': 
                values = sorted([int(item) for item in move[1:].split('/')])
                dance = (1, values)
                n_programs = max(n_programs, values[-1])
            case 'p': 
                dance = (2, sorted(move[1:].split('/')))
        dances.append(dance)
    return dances, n_programs + 1

def solver(dance, n_programs): 
    orders = list()
    orders.append(order_program(dance, 'abcdefghijklmnopqrstuvwxyz'[:n_programs]))
    yield orders[0]
    
    if n_programs == 16 :
        cycle = 1
        while orders[-1] != 'abcdefghijklmnopqrstuvwxyz'[:n_programs]: 
            orders.append(order_program(dance, orders[-1]))
            cycle += 1
        yield orders[1_000_000_000 % cycle - 1]
    else:
        yield order_program(dance, orders[-1])


def order_program(input_, programs): 
    for dance, program in input_:
        match dance:
            case 0: programs = programs[-program:] + programs[:-program]
            case 1: programs = programs[:program[0]] + programs[program[1]] + programs[program[0] + 1: program[1]] + programs[program[0]] + programs[program[1] + 1:]
            case 2: programs = programs.replace(program[0], '_').replace(program[1], program[0]).replace('_', program[1])
    return programs