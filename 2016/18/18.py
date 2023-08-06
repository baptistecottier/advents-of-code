def preprocessing(input_):
    return [0] + [c == '^' for c in input_] +  [0]

def solver(tiles):
    safe_tiles = tiles.count(0) - 2
    for row in range(1, 400_000):
        if row == 40: yield safe_tiles
        tiles       = [0] + [tiles[i] ^ tiles[i + 2] for i in range(len(tiles) - 2)] + [0]
        safe_tiles += tiles.count(0) - 2
    yield safe_tiles