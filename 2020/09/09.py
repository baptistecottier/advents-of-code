def preprocessing(input):
    return [int(item) for item in input.splitlines()]

def solver(input):
    index    = 25
    target   = input[index]
    preamble = input[:25]
    
    while any(target - p in preamble for p in preamble):
        index    += 1
        target   = input[index]
        preamble = input[index - 25: index]
    yield target

    for index in range(len(input)):
        vrange = input[index:][::-1]
        values = []
        while sum(values) < target: 
            values.append(vrange.pop())
        if sum(values) == target: 
            yield min(values) + max(values)
            break
            