from math import lcm

def preprocessing(puzzle_input): 
    grounds     = set()
    trees       = set()
    lumberyards = set()
    
    for y, l in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(l):
            match c: 
                case '.': grounds.add((x, y))
                case '|': trees.add((x, y))
                case '#': lumberyards.add((x, y))
                
    return grounds, trees, lumberyards

def solver(grounds, trees, lumberyards):
    seen_grounds     = [grounds] 
    seen_trees       = [trees]
    seen_lumberyards = [lumberyards]
    total_resources  = list()
    time             = 0
    
    while time < 1_000_000_000:
        grounds, trees, lumberyards = update_landscape(grounds, trees, lumberyards)
        if  grounds in seen_grounds   and \
            trees in seen_trees       and \
            lumberyards in seen_lumberyards:
                    shift  = lcm(seen_trees.index(trees), \
                                 seen_grounds.index(grounds), \
                                 seen_lumberyards.index(lumberyards))
                    period = len(seen_trees) - shift
                    index  = shift + ((1_000_000_000 - shift) % period) - 1
                    yield total_resources[index]
                    break
        else: 
            seen_trees.append(trees)
            seen_grounds.append(grounds)
            seen_lumberyards.append(lumberyards)
            total_resources.append(len(trees) * len(lumberyards))
        time += 1
        if time == 10: yield len(trees) * len(lumberyards)
    
def update_landscape(grounds, trees, lumberyards):
    updated_grounds     = set()
    updated_trees       = set()
    updated_lumberyards = set()
    neighbours          = {(-1, 1),  (0, 1),  (1, 1),\
                           (-1, 0),           (1, 0),\
                           (-1, -1), (0, -1), (1, -1)}
    
    for (x, y) in grounds:
        if sum((x + dx, y + dy) in trees for dx, dy in neighbours) > 2:
            updated_trees.add((x, y))
        else: 
            updated_grounds.add((x, y))
            
    for (x, y) in trees:
        if sum((x + dx, y + dy) in lumberyards for dx, dy in neighbours) > 2:
            updated_lumberyards.add((x, y))
        else: 
            updated_trees.add((x, y))
            
    for (x, y) in lumberyards:
        if any((x + dx, y + dy) in trees       for dx, dy in neighbours) and \
           any((x + dx, y + dy) in lumberyards for dx, dy in neighbours):
            updated_lumberyards.add((x, y))
        else: 
            updated_grounds.add((x, y))
            
    return updated_grounds, updated_trees, updated_lumberyards
    
    
    
    
