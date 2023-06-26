
def parser(input):
    return [floor.count('microchip')+floor.count('generator') for floor in input.splitlines()]

def solver(objects):
    yield move(objects)

    objects[0] += 4
    yield move(objects)

def move(objects): 
    return sum(2 * sum(objects[:x]) - 3 for x in range(1, 4))