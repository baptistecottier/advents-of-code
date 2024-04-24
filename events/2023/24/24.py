from pythonfw.functions import extract_chunks, sign
from itertools          import combinations

def preprocessing(puzzle_input):
    hailstones = extract_chunks(puzzle_input, 6)
    return hailstones


def solver(hailstones):
    l = 200_000_000_000_000
    h = 400_000_000_000_000
    cnt = 0
    temp = set()
    for x, y, _, vx, vy, _ in hailstones:
        a = vy / vx
        b = y - a * x
        temp.add((x, y, a, b, vx))
    for (x, y, a, b, vx), (v, w, c, d, vv) in combinations(temp, 2):
        if a == c: continue
        else : 
            ix = (d - b) / (a - c)
            iy = a * ix + b
            # print(ix, iy)
        if l <= ix <= h and l <= iy <= h: 
            if sign(ix - x) == sign(vx) and sign(ix - v) == sign(vv):
                cnt += 1
    yield cnt