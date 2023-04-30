def generator(input):
    return [int(item) for item in input.splitlines()]

def part_1(input):
    preamble_size = 25
    preamble = input[:preamble_size]
    i = preamble_size
    while any([input[i] - p in preamble for p in preamble]):
        i += 1
        preamble = input[i - preamble_size:i]
    return input[i]


def part_2(input): 
    target = part_1(input)
    for i in range(len(input)):
        values_set = input[i:][::-1]
        values = []
        while sum(values) < target: values.append(values_set.pop())
        if sum(values) == target : return min(values) + max(values)
            