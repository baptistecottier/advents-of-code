from re import findall


def preprocessing(input): 
    paths = []
    max_depth = 0
    rocks = set()
    for path in input.splitlines():
        numbers = list(map(int, findall(r'[0-9]+',path)))
        xa, ya = numbers.pop(0), numbers.pop(0)
        while numbers:
            xa, ya, xb, yb = numbers.pop(0), numbers.pop(0), xa, ya
            if xa == xb: 
                for dy in range(min(ya, yb), max(ya, yb) + 1): rocks.add((xa, dy))
            else: 
                for dx in range(min(xa, xb), max(xa, xb) + 1): rocks.add((dx, ya))
                
    max_depth =  max(y for _, y in rocks) + 2
    for x in range(1000): rocks.add((x, max_depth))
    return rocks

    
def solver(rocks):
    x, y, sand = 500, 0, 0
    endless = True
    max_depth = max(y for _, y in rocks)
    while (500, 0) not in rocks:
        if   (x    , y + 1) not in rocks : y += 1
        elif (x - 1, y + 1) not in rocks : (x , y) = (x - 1, y + 1)
        elif (x + 1, y + 1) not in rocks : (x , y) = (x + 1, y + 1)
        else :
            rocks.add((x, y))
            (x, y) = (500, 0)
            sand   += 1
        if endless and y > max_depth - 2: 
            yield sand
            endless = False
    yield sand
