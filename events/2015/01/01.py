def solver(instructions):
    yield instructions.count('(') - instructions.count(')')
    floor = 0
    for i, c in enumerate(instructions):
        floor += 1 if c == '(' else -1
        if floor < 0:
            yield i + 1
            break