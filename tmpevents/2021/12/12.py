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


def solver(caves): 
    once, twice = get_all_paths(caves).values()
    yield once
    yield once + twice


def get_all_paths(caves, pos = 'start',  path = [], paths_count = {True: 0, False: 0}, twice = True):
    if pos == 'end': 
        paths_count[twice] += 1
        return
    for dst in caves[pos]: 
        if dst.isupper(): 
            get_all_paths(caves, dst, path + [dst], paths_count, twice)
        elif dst.islower() and path.count(dst) <= twice :
            get_all_paths(caves, dst, path + [dst], paths_count, path.count(dst) < twice)
        else: continue
    return paths_count
