"""
Advent of Code - Year 2020 - Day 19
https://adventofcode.com/2020/day/19
"""

# Standard imports
from itertools import product

# Third party imports
from parse import parse, Result


def preprocessing(puzzle_input: str) -> tuple[dict[int, set], list[str]]:
    """
    Parses the input string into a dictionary of resolved patterns and a list of messages based on
    rule definitions.
    """
    patterns = {}
    rules = {}
    plain_rules, messages = (item.splitlines() for item in puzzle_input.split('\n\n'))

    for rule in plain_rules:
        result = parse("{:d}: {}", rule)
        if isinstance(result, Result):
            num, cond = result
            if cond in ['"a"', '"b"']:
                patterns[num] = {cond[1]}
            else:
                rules[num] = [[int(item) for item in c.split(' ')] for c in cond.split(' | ')]

    while 0 not in patterns:
        for num, cond in list(rules.items()):
            if {rule for rules in cond for rule in rules} <= patterns.keys():
                patterns[num] = set()
                for pattern in cond:
                    for combination in product(*[patterns[n] for n in pattern]):
                        patterns[num].add(''.join(list(combination)))
                del rules[num]

    return patterns, messages


def solver(patterns: dict[int, set], messages: list[str]) -> tuple[int, int]:
    """
    Evaluates messages against provided pattern rules and returns a tuple with counts of matches
    for two different rule sets.
    """
    return (len([message for message in messages if message in patterns[0]]),
            sum(looping_rules(message, patterns[8], patterns[11]) for message in messages))


def looping_rules(message: str, rule_eight: set[str], rule_eleven: set[str]) -> bool:
    """
    Checks if a message can be fully matched by repeatedly applying rule_eight at the start and
    rule_eleven in the middle, according to specific substring lengths.
    """
    t = len(next(iter(rule_eight)))
    n = len(next(iter(rule_eleven))) // 2
    while message[:t] in rule_eight:
        candidate = message = message[t:]
        while candidate[:n] + candidate[-n:] in rule_eleven:
            candidate = candidate[n:-n]
            if candidate == '':
                return True
    return False
