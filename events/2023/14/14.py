from collections import defaultdict

def preprocessing(input):
    rnd = set()
    sqr = set()
    hgt = input.count('\n') + 1
    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line):
            match c:
                case 'O': rnd.add((x, hgt - y))
                case '#': sqr.add((x, hgt - y))
    return rnd, sqr, x + 1, hgt

def solver(rnd, sqr, w, h):
    loads = list()
    rnd = tilt_n(rnd, sqr, h)
    yield sum(y for _, y in rnd)
    
    rnd = tilt_w(rnd, sqr)
    rnd = tilt_s(rnd, sqr)
    rnd = tilt_e(rnd, sqr, w)
    loads.append(sorted(rnd))
    while True:
        rnd = tilt_n(rnd, sqr, h)
        rnd = tilt_w(rnd, sqr)
        rnd = tilt_s(rnd, sqr)
        rnd = tilt_e(rnd, sqr, w)
        if rnd not in loads : loads.append(rnd)
        else : 
            stt = loads.index(rnd)
            prd = len(loads) - stt
            idx = stt + (1_000_000_000 - stt) % prd - 1
            yield sum(y for _, y in loads[idx])
            break

def tilt_n(rnd, sqr, h):
    tlt = set()
    for x, y in rnd:
        while (x, y) not in sqr and y <= h : y += 1
        y -= 1
        while (x, y) in tlt : y -= 1
        tlt.add((x, y))
    return tlt

def tilt_w(rnd, sqr):
    tlt = set()
    for x, y in rnd:
        while (x, y) not in sqr and x >= 0 : x -= 1
        x += 1
        while (x, y) in tlt : x += 1
        tlt.add((x, y))
    return tlt

def tilt_s(rnd, sqr):
    tlt = set()
    for x, y in rnd:
        while (x, y) not in sqr and y > 0 : y -= 1
        y += 1
        while (x, y) in tlt : y += 1
        tlt.add((x, y))
    return tlt

def tilt_e(rnd, sqr, w):
    tlt = set()
    for x, y in rnd:
        while (x, y) not in sqr and x < w : x += 1
        x -= 1
        while (x, y) in tlt : x -= 1
        tlt.add((x, y))
    return tlt