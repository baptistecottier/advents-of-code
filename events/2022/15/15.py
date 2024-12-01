from itertools          import chain, product
from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input): 
    sensors = extract_chunks(puzzle_input, 4)
    sensors = {(xs, ys, abs(xb - xs) + abs(yb - ys)) for xs, ys, xb, yb in sensors}
    return sensors


def solver(sensors, max_size = 4_000_000):
    cnt = set()
    
    for xs, ys, md in sensors:
            cnt.add(range(xs - (md - abs(ys - max_size // 2)) , 1 + xs + (md - abs(ys - max_size // 2))))
    yield len(set(list(chain.from_iterable(cnt)))) - 1


    for x , y in product(range(0, max_size) , repeat = 2):
        if all((abs(xs - x) + abs(ys - y)) > md for xs, ys, md in sensors): 
            yield 4_000_000 * x + y 
            break