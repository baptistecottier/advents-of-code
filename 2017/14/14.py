from pythonfw.y2017 import knot_hash


def solver(salt):
    
    maze = set()
    for row in range(128):
        hex_hash = int(knot_hash(f"{salt}-{row}",256), 16)
        maze.update(set((row, i) for i in range(128) if hex_hash >> i & 1))
    
    yield len(maze)
    
    regions = 0
    while maze:
        region = [maze.pop()]
        while region:
            (x, y) = region.pop()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                candidate = x + dx, y + dy
                if candidate in maze:
                    region.append(candidate)
                    maze.remove(candidate)
        regions += 1
        
    yield regions