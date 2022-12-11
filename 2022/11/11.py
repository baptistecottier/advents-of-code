from math import prod

def generator(input):
    monkeys = input.split('\n\n')
    starting_items = []
    ops = []
    pred = []
    for i , monkey in enumerate(monkeys) : 
        details = monkey.splitlines()[1:]
        items = details[0].split(': ')[1]
        starting_items+=[[int(item),i] for item in items.split(', ')]
   
        match (details[1].split('= old ')[1]).split(' ') :
            case ('*', 'old') : ops.append([0,0,1])
            case ('*', n) :  ops.append([0, int(n), 0])
            case (_, n) : ops.append([int(n), 1, 0])
            
        pred.append([int(line.split(' ')[-1]) for line in details[2:]])
    return [starting_items, ops, pred]
    
def part_1(input) : 
    return  solver(input, 20, 3)

def part_2(input) : 
   return  solver(input, 10_000, 1)
    
def solver(input, rounds, div):
    [items, ops, tests] = input
    modulo =  prod([pred[0] for pred in tests])
    inspected_items = [0  for _ in range(len(ops))]
    for [item, new_monkey] in items : 
        for _ in range(rounds):
            old_monkey = 0
            while new_monkey >= old_monkey :
                add, mul, sq = ops[new_monkey]
                pred = tests[new_monkey]
                inspected_items[new_monkey] += 1
                item = (((item * mul + sq * item * item) + add) // div) % (div * modulo)
                old_monkey, new_monkey = new_monkey, pred[1 + (item % pred[0] != 0)]
                
    return prod(sorted(inspected_items)[-2:])
            