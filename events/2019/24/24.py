def preprocessing(puzzle_input):
    bugs = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, b in enumerate(line):
            if b == '#': bugs.add((x, y))
    return bugs

def solver(bugs):
    visited = set()
    n = state_to_int(bugs)
    while n not in visited:
        visited.add(n)
        new = set()
        for x in range(5):
            for y in range(5):
                infested = sum(((x + a, y + b) in bugs) for (a, b) in [(-1, 0), (1, 0), (0, -1), (0, 1)])
                if infested == 1 or ((x, y) not in bugs and infested ==2):
                        new.add((x, y))
        bugs = new.copy()
        n = state_to_int(bugs)
    yield state_to_int(bugs)

def state_to_int(state):
    n = 0
    for x, y in state:
        n += 2 ** (x + 5 * y)
    return n

def int_to_state(n):
    bugs = set()
    for i in range(25):
        if (n>>i) & 1: bugs.add((i % 5, i // 5))
    return bugs