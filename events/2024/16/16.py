from collections import deque, defaultdict

def preprocessing(puzzle_input):
    kiosk = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            match c:
                case '#': kiosk.add((x, y))
                case 'S': start = (x, y)
                case 'E': end = (x,y)
                case _  : pass
    return kiosk, start, end


def solver(kiosk, start, end):
    paths = deque([[(start, (1, 0), 0,)]])
    scores = defaultdict(lambda : 1_000_000)
    best_paths_tiles = set()
    max_score = 1_000_000
    
    while paths:
        path = paths.popleft()
        (x, y), (dx, dy), path_score = path[-1]
        if (x, y) == end:
            if path_score == max_score:
                best_paths_tiles.update(pos for (pos, _, _) in path)
            elif path_score < max_score:
                best_paths_tiles = set([pos for (pos, _, _) in path])
                max_score = path_score
        else:
            for vx, vy in ((dx, dy), (-dy, dx), (dy, -dx)):
                pos = x + vx, y + vy
                pos_score = scores[pos]
                if path_score <= pos_score + 1_000 and pos not in kiosk:
                    delta = 1 if vx == dx else 1_001
                    paths.append(path + [(pos, (vx, vy), path_score + delta)])
                    scores[pos] = min(pos_score, path_score + delta)
    yield max_score
    yield len(best_paths_tiles)