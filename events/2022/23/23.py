def preprocessing(puzzle_input):
    elves = list()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == '#': elves.append((x, y))
    return elves

from copy import deepcopy
from collections import Counter

def solver(elves):
    neighbours = {(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)}
    N = [{(-1, -1), (0, -1), (1, -1)}, {(-1, 1), (0, 1), (1, 1)},\
         {(-1, -1), (-1, 0), (-1, 1)}, {(1, -1), (1, 0), (1, 1)}]
    dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    i = -1
    while True:
        i += 1
        print(i)
        new_elves = []
        for (x, y) in elves:
            if all((x + dx, y + dy) not in elves for (dx, dy) in neighbours):
                new_elves.append((x, y))
                continue
            elif all((x + dx, y + dy)not in elves for (dx, dy) in N[i % 4]):
                dx, dy = dir[i % 4]
            elif all((x + dx, y + dy)not in elves for (dx, dy) in N[(i + 1) % 4]):
                dx, dy = dir[(i + 1) % 4]
            elif all((x + dx, y + dy)not in elves for (dx, dy) in N[(i + 2) % 4]):
                dx, dy = dir[(i + 2) % 4]
            elif all((x + dx, y + dy)not in elves for (dx, dy) in N[(i + 3) % 4]):
                dx, dy = dir[(i + 3) % 4]
            else:
                new_elves.append((x, y))
                continue
                
            new_elves.append((x + dx, y + dy))
        relves = []

        cnts = Counter(new_elves)
        for k in range(len(elves)):
            if cnts[new_elves[k]] > 1:
                relves.append(elves[k])
            else:
                relves.append(new_elves[k])
                
        if set(elves) == set(relves):
            yield i + 1
            break
            
        elves = relves

        if i == 9:
            minx = min(x for (x, _) in elves)
            maxx = max(x for (x, _) in elves)
            miny = min(y for (x, y) in elves)
            maxy = max(y for (x, y) in elves)
            yield (maxx - minx + 1)*(maxy - miny + 1) - len(elves)

        
            