from parse import parse

def preprocessing(puzzle_input):
    infos = puzzle_input.split('\n\n')
    starting_state, trigger = parse("Begin in state {}.\nPerform a diagnostic checksum after {:d} steps.", infos[0])
    details = []
    for state in infos[1:]:
        a, b, c, d, e, f, g = parse("In state {}:\n  If the current value is 0:\n    - Write the value {:d}.\n    - Move one slot to the {}.\n    - Continue with state {}.\n  If the current value is 1:\n    - Write the value {:d}.\n    - Move one slot to the {}.\n    - Continue with state {}.", state)
        details.append([[b,c == 'left',ord(d) - 65],[e, f == 'left', ord(g) - 65]])
    return ord(starting_state) - 65, trigger, details

def solver(state, trigger, details): 
    tape = [0 for _ in range(trigger)]
    pos = 0
    for i in range(trigger):
        infos = details[state]
        current_value = tape[pos]
        tape[pos] = infos[current_value][0]
        pos = pos + 1 - 2 * infos[current_value][1] % trigger
        state = infos[current_value][2]
    yield sum(tape)