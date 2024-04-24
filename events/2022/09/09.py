from pythonfw.functions import sign


def preprocessing(puzzle_input):
    x, y = 0, 0
    path = [[x,y]]
    orientation = {'D': (0, -1), 'L': (-1, 0),  'R': (1, 0), 'U': (0, 1)}

    for dir, step in [ins.split(' ') for ins in puzzle_input.splitlines()]:
        step = int(step)
        (dx , dy) = orientation[dir]
        path.extend((x + i * dx , y + i * dy) for i in range(1, step + 1))
        (x , y) = (x + step * dx, y + step * dy)

    return path


def solver(path):
    for knot in range(9):
        tx , ty = 0 , 0
        visited = []
        for (hx, hy) in path:
            if abs(hy - ty) > 1 or abs(hx - tx) > 1:
                tx += sign(hx - tx)
                ty += sign(hy - ty)
            visited.append((tx, ty))
        path = visited
        if knot in [0, 8]: yield len(set(visited))