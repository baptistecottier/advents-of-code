from itertools import product

def generator(input):
    lights = set()
    grid = input.splitlines()
    for (x, y) in product(range(100), repeat = 2):
        if grid[y][x] == '#': lights.add((x, y))
    return lights 

def part_1(lights): 
    return apply_steps(lights, set())

def part_2(lights): 
    return apply_steps(lights, {(0, 0), (0, 99), (99, 0), (99, 99)})


def apply_steps(lights, always_on):
    neighbours = {(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)}
    lights = lights.union(always_on)
    for _ in range(100):
        updated_lights = always_on.copy()
        for (x, y) in product(range(100), repeat = 2):
            match sum((x + dx, y + dy) in lights for (dx, dy) in neighbours):
                case 3: 
                    updated_lights.add((x, y))
                case 2: 
                    if (x, y) in lights: updated_lights.add((x, y))
        lights = updated_lights
    return len(lights)
    