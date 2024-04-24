from itertools import product
from math      import prod
from dataclasses import dataclass
from itertools import combinations


@dataclass
class Border:
    N: set
    E: set
    S: set
    W: set

@dataclass(unsafe_hash=True)
class Tile:
    id: int
    borders: Border
    body: dict
    score: dict 
    rotate: int = 0
    flip: int = 0

def get_borders(body, size):
    borders = {(x, y) for (x, y) in body if x in [0, size - 1] or y in [0, size - 1]}
    north = {x for (x, y) in borders if y == 0}
    east = {y for (x, y) in borders if x == size - 1}
    south = {x for (x, y) in borders if y == size - 1}
    west = {y for (x, y) in borders if x == 0}
    return Border(north, east, south, west)

def preprocessing(puzzle_input):
    tiles      = list()
    list_tiles = [item.splitlines() for item in puzzle_input.split('\n\n')]
    size       = len(list_tiles[0]) - 1
    score = {(a, b, c): set() for a, b, c in product((0, 1, 2, 3), (0, 1), (0, 1))}
    print(score)
    for tile in list_tiles:
        id = int(tile[0].split(' ')[1][:-1])
        body = {(x, y) for x, y in product(range(len(tile[1])),range(len(tile) - 1)) if tile[y + 1][x] == '#'}
        border = {(0,0, 0) : get_borders(body, size), (0, 1, 0) : get_borders(flipv(body, size), size), (0, 0, 1) : get_borders(fliph(body, size), size), (0, 1, 1) : get_borders(flipv(fliph(body, size), size), size)}
        for r in [1, 2, 3]:
            body = rotate(body, size)
            border[(r, 0, 0)] = get_borders(body, size)
            border[(r, 1, 0)] = get_borders(flipv(body, size), size)
            border[(r, 0, 1)] = get_borders(fliph(body, size), size)
            border[(r, 1, 1)] = get_borders(flipv(fliph(body, size), size), size)
        tiles.append(Tile(id, border, body, score))
    return size, tiles

def rotate(coords, size):
    return {(abs(size - y - 1), x) for (x, y) in coords}  

def flipv(coords, size):
    return {(size - 1 - x, y) for (x, y) in coords}  

def fliph(coords, size):
    return {(x, size - 1 - y) for (x, y) in coords}  

def display(coords, size):
    for y in range(size):
        line = ""
        for x in range(size):
            if (x, y) in coords : line+='#'
            else : line += '.'
        print(line)

def solver(size, tiles: Tile):
    for ta, tb in combinations(tiles, 2):
        ba : dict = ta.borders
        bb : dict = tb.borders

        for ((ra, fva, fha), pa), ((rb, fvb, fhb), pb) in product(ba.items(), bb.items()):
            boo = border_match(pa, pb)
            if boo : 
                ta.score[(ra, fva, fha)].add(tb.id)
                tb.score[(rb, fvb, fhb)].add(ta.id)
                break
    for tile in tiles: 
        print(tile.id, sum(len(x) for x in tile.score.values()))
    yield 2
 
    
def border_match(pa, pb):
    return (pa.N == pb.S) or (pa.S == pb.N) or (pa.E == pb.W) or (pa.W == pb.E)