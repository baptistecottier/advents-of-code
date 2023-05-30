def generator(input):
    return [c == '^' for c in input]

def part_1(tiles): 
    return count_safe_tiles(tiles, 40)

def part_2(tiles): 
    return count_safe_tiles(tiles, 400_000)


def count_safe_tiles(tiles, rows):
    safe_tiles = tiles.count(0)
    tiles      = [0] + tiles + [0]
    for _ in range(rows - 1):
        tiles       = [0] + [tiles[i] ^ tiles[i + 2] for i in range(len(tiles) - 2)] + [0]
        safe_tiles += tiles.count(0) - 2
    return safe_tiles