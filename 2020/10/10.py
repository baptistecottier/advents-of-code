def preprocessing(input):
    joltages = sorted(int(item) for item in sorted(input.splitlines()))
    return [0] + joltages + [joltages[-1] + 3]

def solver(joltages):
    differences = [b - a for a, b in zip(joltages[:-1], joltages[1:])]
    yield differences.count(3) * differences.count(1)

    groups = 1
    while differences:
        size = 0
        while differences and differences.pop() == 1: size += 1
        if size > 1: groups *= (2 ** (size - 1) - (size == 4)) 
    yield groups