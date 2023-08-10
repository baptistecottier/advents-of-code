def preprocessing(input): 
    tiles = set()
    for tile in input.splitlines():
        n = {}
        for value in ['se', 'sw', 'ne', 'nw', 'e', 'w']:
            n[value] = tile.count(value)
            tile = tile.replace(value,'')
        x = n['e'] - n['w'] + 0.5 * (n['se'] + n['ne']) - 0.5 * (n['sw'] + n['nw'])
        y = n['nw'] + n['ne'] - (n['sw'] + n['se'])
        if (x, y) in tiles:
            tiles.remove((x, y))
        else:
            tiles.add((x, y))
    return tiles
    

def solver(input):
    yield len(input)
    
    neighbours = {(0.5, -1), (-0.5, -1), (0.5, 1), (-0.5, 1), (1, 0), (-1, 0)}
    tiles = input
    
    for d in range(100):
        tested = set()
        updated_tiles = set()
        for x, y in tiles:
            if sum((x + dx, y + dy) in tiles  for dx, dy in neighbours) in [1, 2]:
                updated_tiles.add((x, y))
            for tx, ty in neighbours:
                xx = x + tx
                yy = y + ty
                if (xx, yy) not in tiles and (xx, yy) not in tested:
                    tested.add((xx, yy))
                    if sum((xx + dx, yy + dy) in tiles  for dx, dy in neighbours) == 2: updated_tiles.add((xx, yy))
        tiles = updated_tiles
    yield len(tiles)