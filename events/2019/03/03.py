from pythonfw.classes import Point

def preprocessing(puzzle_input): 
    return [[[item[0], int(item[1:])] for item in wire.split(',')] for wire in puzzle_input.splitlines()]


def solver(paths):
    dir: dict = {'L': (-1, 0), 'U': (0, -1), 'R': (1, 0), 'D': (0, 1)}
    
    pos: Point = Point()
    step: int  = 0
    path: dict = {pos.xy(): step}
    for turn, steps in paths.pop(0):
        dx, dy = dir[turn]
        for _ in range(steps):
            pos.move(dx, dy)
            path[pos.xy()] = (step := step + 1)

    pos  = Point()
    step = 0
    distances: set      = set()
    combined_steps: set = set()
    
    for turn, steps in paths.pop(0):
        dx, dy = dir[turn]
        for _ in range(steps):
            step += 1
            pos.move(dx, dy)
            if pos.xy() in path: 
                distances.add(pos.manhattan())
                combined_steps.add(path[pos.xy()] + step)

    yield min(distances)
    yield min(combined_steps)