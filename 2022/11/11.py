from math import prod

def preprocessing(input):
    monkeys        = input.split('\n\n')
    starting_items = []
    funcs          = []
    pred           = []
    
    for i, monkey in enumerate(monkeys): 
        details        = monkey.splitlines()[1:]
        items          = details[0].split(': ')[1]
        starting_items += [[int(item), i] for item in items.split(', ')]
   
        match (details[1].split('= old ')[1]).split(' '):
            case ('*', 'old'): funcs.append(lambda x: x ** 2)
            case ('*', n    ): funcs.append(lambda x, n = int(n): x * n)
            case (_  , n    ): funcs.append(lambda x, n = int(n): x + n)
            
        pred.append(tuple(int(line.split(' ')[-1]) for line in details[2:]))
    return starting_items, funcs, pred


def solver(items, funcs, tests):
    yield monkey_business(items, funcs, tests, 20, 3)
    yield monkey_business(items, funcs, tests, 10_000, 1)
    
    
def monkey_business(items, funcs, tests, rounds, div):
    modulo          = prod([mod for mod, _, _ in tests])
    inspected_items = [0  for _ in funcs]

    for old, new_monkey in items: 
        for _ in range(rounds):
            old_monkey = 0
            while new_monkey >= old_monkey:
                func = funcs[new_monkey]
                pred = tests[new_monkey]
                inspected_items[new_monkey] += 1
                old = (func(old) // div) % (div * modulo)
                old_monkey, new_monkey = new_monkey, pred[1 + (old % pred[0] != 0)]
                
    return prod(sorted(inspected_items)[-2:])
            