def preprocessing(puzzle_input):
    return [int(item) for item in puzzle_input.splitlines()]

def solver(puzzle_input):
    index    = 25
    target   = puzzle_input[index]
    preamble = puzzle_input[:25]
    
    while any(target - p in preamble for p in preamble):
        index    += 1
        target   = puzzle_input[index]
        preamble = puzzle_input[index - 25: index]
    yield target

    for index in range(len(puzzle_input)):
        vrange = puzzle_input[index:][::-1]
        values = []
        while sum(values) < target: 
            values.append(vrange.pop())
        if sum(values) == target: 
            yield min(values) + max(values)
            break
            