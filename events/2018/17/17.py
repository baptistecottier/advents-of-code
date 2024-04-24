from re                 import findall
from pythonfw.functions import extract_chunks
from pythonfw.classes   import Point

def preprocessing(puzzle_input: str):
    clay = set()
    numbers = extract_chunks(puzzle_input, 3)
    for cl, (a, b, c) in zip(puzzle_input.splitlines(), numbers):
        if cl.startswith('x'):
            clay.update({(a, y) for y in range(b, c + 1)})
        else: 
            clay.update({(x, a) for x in range(b, c + 1)})
    return clay

def solver(clay):
    water = Point(500, 0)
    start = len(clay)
    max_y = max(y for _, y in clay)
    yield 1
    while water.y < max_y:
        if (water.x, water.y + 1) in clay:
            lx = water.x - 1
            rx = water.x + 1
            while (lx, water.y) not in clay: lx -= 1
            while (rx, water.y) not in clay: ly += 1
            clay.update({(x, water.y) for x in range(lx + 1, rx)})
            water.move(0, -1)
        else: water.move(0, 1)