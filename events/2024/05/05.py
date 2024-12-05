from itertools import permutations

def preprocessing(puzzle_input):
    rules, updates = puzzle_input.split('\n\n')
    rules = list([int(item) for item in rule.split('|')] for rule in rules.splitlines())
    updates = list([int(item) for item in update.split(',')] for update in updates.splitlines())
    return rules, updates

def solver(rules, updates):
    middle = 0
    to_modify = []
    for u in updates:
        for a, b in list(zip(u[:-1], u[1:])):
            count = 1
            if [a, b] not in rules:
                count = 0
                to_modify.append(u)
                break
        middle = middle + count *  u[len(u)//2]
    yield middle
    
    middle = 0
    while to_modify:
        u = to_modify.pop()
        count = 1
        for i in range(len(u) - 1):
            if [u[i], u[i + 1]] not in rules:
                a = u[i]
                b = u[i + 1]
                u[i] = b
                u[i + 1] = a
                to_modify.append(u)
                count = 0
                break
        middle = middle + count *  u[len(u)//2]
    yield middle

        
            
            