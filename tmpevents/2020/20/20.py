from itertools import product
from math      import prod
def preprocessing(input):
    tiles = {}
    for tile in [item.splitlines() for item in input.split('\n\n')]:
        id = int(tile[0].split(' ')[1][:-1])
        tiles[id] = {(x, y) for x, y in product(range(len(tile[1])),range(len(tile) - 1)) if tile[y + 1][x] == '#'}
    return tiles
      
              
def solver(input): 
    sides = {}
    for id, tile in input.items():
        sides[id] = []
        for xx in [0, 9]:
            slide = {(x, y) for (x, y) in tile if x == xx}
            sides[id].append(slide)                            # Initial position
            sides[id].append({(x, 9 - y) for (x, y) in slide}) # Horizontal flip
            sides[id].append({(9 - x, y) for (x, y) in slide}) # Vertical flip
            
            sides[id].append({(9 - y, 9 - x) for (x, y) in slide}) # 90 degrees rotation
            sides[id].append({(9 - x, 9 - y) for (x, y) in slide}) # 180 degrees rotation
            sides[id].append({(y, x) for (x, y) in slide}) # 270 degrees rotation
            
        for yy in [0, 9]:
            slide = {(x, y) for (x, y) in tile if y == yy}
            sides[id].append(slide)                            # Initial position
            sides[id].append({(x, 9 - y) for (x, y) in slide}) # Horizontal flip
            sides[id].append({(9 - x, y) for (x, y) in slide}) # Vertical flip
            
            sides[id].append({(9 - y, 9 - x) for (x, y) in slide}) # 90 degrees rotation
            sides[id].append({(9 - x, 9 - y) for (x, y) in slide}) # 180 degrees rotation
            sides[id].append({(y, x) for (x, y) in slide}) # 270 degrees rotation
    all_sides = []
    cnt = {}
    for item in sides.values():
            all_sides += item
    for id in sides.keys():
        cnt[id] = 0
        for item in all_sides:
            if item in sides[id]:
                cnt[id] += 1
    test = {k: v for k, v in sorted(cnt.items(), key=lambda item: item[1])}
    yield prod(list(test.keys())[:4])