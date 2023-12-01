from pythonfw.classes import Point


def preprocessing(input):
    trees = set()
    for y, row in enumerate(input.splitlines()):
        for x, c in enumerate(row):
            if c == '#': trees.add((x, y))
    return trees, x + 1, y


def solver(trees, mx, my):
    total = 1
    for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        pos = Point()
        cnt = 0
        while pos.y <= my: 
            if (pos.x % mx, pos.y) in trees: cnt += 1
            pos.move(dx, dy)
        if dx == 3: yield cnt
        total *= cnt
    yield total