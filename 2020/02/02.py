from hashlib import new
from typing import Generator
from parse import parse

def preprocessing(input: str) -> Generator[tuple[int, int, str, str], None, None]: 
    return (parse("{:d}-{:d} {}: {}", pw) for pw in input.splitlines())

def solver(passwords: Generator[tuple[int, int, str, str], None, None]):
    old_rule: int = 0
    new_rule: int = 0
    for a, b, w, pw in passwords:
        if a <= pw.count(w) <= b: old_rule += 1
        if (pw[a-1] == w) ^ (pw[b-1] == w): new_rule += 1
    yield old_rule
    yield new_rule
