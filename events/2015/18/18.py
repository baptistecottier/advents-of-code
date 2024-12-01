from itertools import product


def preprocessing(input_):
    lights = set()
        
    for y, line in enumerate(input_.splitlines()):
        for x, c in enumerate(line):
            if c == '#': lights.add((x, y))
    return lights, x, y


def solver(lights, x, y, iterations = 100):
    yield apply_steps(lights, x, y, set(), iterations)
    yield apply_steps(lights, x, y, {(0, 0), (0, y), (x, 0), (x, y)}, iterations)
        

def apply_steps(lights, x, y, always_on, iterations):
    neighbours = {(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)}
    lights     = lights.union(always_on)
    
    for _ in range(iterations):
        updated_lights = always_on.copy()
        for (x, y) in product(range(x + 1), range(y + 1)):
            match sum((x + dx, y + dy) in lights for (dx, dy) in neighbours):
                case 3: 
                    updated_lights.add((x, y))
                case 2: 
                    if (x, y) in lights: updated_lights.add((x, y))
        lights = updated_lights
        
    return len(lights)