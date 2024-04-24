from parse import parse
from itertools import product 

def preprocessing(puzzle_input): 
    patterns = {}
    rules = {}
    plain_rules, messages = (item.splitlines() for item in puzzle_input.split('\n\n'))
    for rule in plain_rules:
        num, cond = list(parse("{:d}: {}", rule))
        if cond in ['"a"', '"b"']: patterns[num] = {cond[1]}
        else: rules[num] = [[int(item) for item in c.split(' ')] for c in cond.split(' | ')]
    while 0 not in patterns:
        for num, cond in list(rules.items()):
                if not any(pattern not in patterns for pattern in [rule for rules in cond for rule in rules]):
                    patterns[num] = set()
                    for pattern in cond:
                        for combination in product(*[patterns[n] for n in pattern]):
                            patterns[num].add(''.join(list(combination)))
                    del rules[num]
    return patterns[0], patterns[8], patterns[11], messages

def solver(rule, rule_eight, rule_eleven, messages):
    yield len([message for message in messages if message in rule])
    yield sum(looping_rules(message, rule_eight, rule_eleven) for message in messages)

def looping_rules(message, rule_eight, rule_eleven):
    t = len(next(iter(rule_eight)))
    n = len(next(iter(rule_eleven))) // 2
    while message[:t] in rule_eight:
        candidate = message = message[t:]
        while candidate[:n] + candidate[-n:] in rule_eleven:
            candidate = candidate[n:-n]
            if candidate == '': return True
    return False