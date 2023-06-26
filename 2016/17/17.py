from _md5 import md5

def solver(salt):
    paths = find_paths(salt, paths = [])
    yield paths.pop(0)
    yield len(paths.pop())

def find_paths(path, paths, pos = (0, 0)):
    if pos == (3, 3): paths.append(path[8:])
    else:
        x, y = pos
        for (n, dx, dy) in get_neighbours(path):
            if  0 <= x + dx <= 3 and 0 <= y + dy <= 3: 
                find_paths(path + n, paths, (x + dx, y + dy))
    return sorted(paths , key = len)

def get_neighbours(s): 
    hash       = md5(s.encode()).hexdigest()[:4]
    neighbours = [('U', 0, -1), ('D', 0, 1), ('L', -1, 0), ('R', 1, 0)] 
    return (neighbour for i, neighbour in enumerate(neighbours) if 'b' <= hash[i] <= 'f')