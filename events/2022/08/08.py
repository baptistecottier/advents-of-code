from itertools import product


def preprocessing(puzzle_input): 
    trees = []
    for y, row in enumerate(puzzle_input.splitlines()):
        heights = []
        for x, height in enumerate(row):
            heights.append(height)
        trees.append(heights)
    return trees


def solver(trees):
    width      = len(trees[0])
    depth      = len(trees)
    visible    = set()
    max_scenic = 0
    
    for x, y in product(range(1, depth - 1), range(1, width - 1)):
        scenic = 1
        height = trees[y][x]
        for dx, dy in {(0, 1), (1, 0), (0, -1), (-1, 0)}:
            nb_trees = 1
            tx, ty   = x + dx, y + dy
            while trees[ty][tx] < height: 
                if (tx:= tx + dx) in [-1, width] or (ty:= ty + dy) in [-1, depth]: 
                    visible.add((x, y))
                    break
                nb_trees += 1
            scenic *= nb_trees
        if scenic > max_scenic: max_scenic = scenic
                
    yield 2 * (width + depth - 2) + len(visible)
    yield max_scenic

            