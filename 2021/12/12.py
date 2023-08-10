from copy import deepcopy


def preprocessing(input):
    paths = {}
    for path in input.splitlines():
        start, end = path.split('-')
        if end != 'start':
            if start in paths: paths[start].append(end)
            else: paths[start] = [end]
        if start != 'start':
            if end in paths: paths[end].append(start)
            else: paths[end] = [start]
    return paths 

def solver(input_): 
    yield part_1(deepcopy(input_))
    yield part_2(deepcopy(input_))

def part_1(input): 
    return len(complete_paths(input, 'start', [], [], twice = False))

def part_2(input): 
    return len(complete_paths(input, 'start', [], [], twice = True))

def complete_paths(caves, pos,  path, list_paths, twice):
    if pos == 'end': return list_paths.append(path)
    for dst in caves[pos]: 
        if dst.isupper(): 
            complete_paths(caves, dst, path + [dst], list_paths, twice)
        elif dst.islower() and path.count(dst) <= twice :
            complete_paths(caves, dst, path + [dst], list_paths, path.count(dst) < twice)
        else: continue
    return list_paths
