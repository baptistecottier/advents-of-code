def generator(file) :
    return [int(x) for x in file.splitlines()]

def part_1(input) : 
    return sum(input)

def part_2(input) : 
    visited_frequencies = []
    current = 0
    i = 0
    while current not in visited_frequencies :
        visited_frequencies.append(current)
        current += input[i]
        i = (i + 1) % len(input)
    return current