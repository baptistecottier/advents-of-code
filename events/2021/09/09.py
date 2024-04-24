from math        import prod
from collections import defaultdict

def preprocessing(puzzle_input):
    cave = defaultdict(lambda: 9)
    for y, row in enumerate(puzzle_input.splitlines(), 1):
        for x, n in enumerate(row, 1):
            cave[(x, y)] = int(n)
    return cave

def solver(cave): 
    neighbours = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    low_points = {(x, y) for x, y in list(cave) if all(cave[(x, y)] < cave[(x + dx, y + dy)] for dx, dy in neighbours)}
    yield len(low_points) + sum(cave[pos] for pos in low_points)
    yield prod(sorted(basin_size(cave, pos, set()) for pos in low_points)[-3:])  
  
    
def basin_size(cave, pos, visited):
    x, y = pos
    if cave[(x, y)] == 9 or (x, y) in visited: return 0
    else: 
        visited.add(pos)
        return 1 + sum(basin_size(cave, (x + dx, y + dy), visited) for dx, dy in {(-1, 0), (0, 1), (1, 0), (0, -1)})