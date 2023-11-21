from hashlib import new
from parse   import parse


def preprocessing(input: str): 
    return [parse("{:d}-{:d} {}: {}", pw) for pw in input.splitlines()]


def solver(passwords):
    old_rule: int = 0
    new_rule: int = 0
    for a, b, w, pw in passwords:
        if a <= pw.count(w) <= b: old_rule += 1
        if (pw[a-1] == w) ^ (pw[b-1] == w): new_rule += 1
    yield old_rule
    yield new_rule
