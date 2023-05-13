def generator(input): 
    coordinates, instructions = input.split('\n\n')
    coordinates = {tuple(int(item) for item in point.split(',')) for point in coordinates.splitlines()}
    instructions = [(ins[11] , int(ins[13:])) for ins in instructions.splitlines()]
    return (coordinates, instructions)

def part_1(input): 
    return len(fold(input[0], input[1][:1]))

def part_2(input): 
    return '\n'.join(''.join([' ', '█'][(x, y) in fold(*input)] for x in range(40)) for y in range(6))

def fold(coordinates, instructions): 
    for (axis, n) in instructions:
        if axis == 'x': coordinates = {(min(x, 2 * n - x), y) for (x, y) in coordinates}
        if axis == 'y': coordinates = {(x, min(y, 2 * n - y)) for (x, y) in coordinates}
    return coordinates

