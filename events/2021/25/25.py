def preprocessing(puzzle_input):
    west  = set()
    south = set()
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(row):
            match c:
                case '>': west.add((x, y))
                case 'v': south.add((x, y))
    return west, south, x + 1, y + 1

def solver(cucumbers):
    west, south, w, h = cucumbers
    steps = 0
    while steps := steps + 1:
        old_west  = west
        old_south = south
        occupied = west.union(south)
        west  = {((x + 1) % w, y) if ((x + 1) % w, y) not in occupied else (x, y) for (x, y) in west}
        occupied = west.union(south)
        south = {(x, (y + 1) % h) if (x, (y + 1) % h) not in occupied else (x, y) for (x, y) in south}
        if old_west == west and old_south == south: break
    yield steps
