
def generator(input):
    return [floor.count('microchip')+floor.count('generator') for floor in input.splitlines()]

def part_1(objects): 
    return move(objects)

def part_2(objects):
    objects[0] += 4
    return move(objects)


def move(objects): 
    return sum(2 * sum(objects[:x]) - 3 for x in range(1, 4))