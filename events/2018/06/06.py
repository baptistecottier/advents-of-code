from itertools import product

def preprocessing(puzzle_input):
    coordinates    = set(tuple(int(item) for item in line.split(', ')) for line in puzzle_input.splitlines())
    list_x, list_y = zip(*coordinates)
    min_x, min_y   = min(list_x), min(list_y)
    max_x, max_y   = max(list_x), max(list_y)
    return coordinates, min_x, max_x, min_y, max_y

def solver(coordinates, min_x, max_x, min_y, max_y):
    areas   = {c: 0 for c in coordinates}
    corners = set()
    region_size = 0
    
    for (x, y) in product((min_x, max_x), (min_y, max_y)):
        corners.add(min(coordinates, key = lambda c : abs(c[0] - x) + abs(c[1] - y)))

    for x, y in product(range(min_x, max_x), range(min_y, max_y)):
        distances = list()
        for xx, yy in coordinates:
            distances.append(abs(xx - x) + abs(yy - y))
        if sum(distances) < (10_000 if len(coordinates) == 50 else 32): 
            region_size += 1
        mx, my = min(coordinates, key = lambda c: abs(c[0] - x) + abs(c[1] - y))
        if distances.count(abs(mx - x) + abs(my - y)) == 1: areas[(mx, my)] += 1

    yield max(areas[c] for c in coordinates if c not in corners)
    yield region_size