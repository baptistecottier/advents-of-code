from parse import parse
import itertools 
from pythonfw.functions import extract_chunks

def preprocessing(input): 
    sensors = extract_chunks(input, 4)
    sensors = {(xs, ys, abs(xb-xs) + abs(yb-ys)) for xs, ys, xb, yb in sensors}
    return sensors

def solver(sensors):
    size = 4_000_000
    cnt = set()
    for xs, ys, md in sensors:
            cnt.add(range(xs - (md - abs(ys - size // 2)) , 1 + xs + (md - abs(ys - size // 2))))
    yield len(set(list(itertools.chain.from_iterable(cnt)))) - 1

    for x , y in itertools.product(range(0,size) , repeat = 2):
        if all(abs(xs - x) + abs(ys - y) > md for [xs, ys, md] in sensors): 
            yield size * x + y 
            break