def preprocessing(puzzle_input):
    patterns = list()
    for raw_tile in puzzle_input.split('\n\n'):
        pattern = dict()
        for y, line in enumerate(raw_tile.splitlines()):
            for x, c in enumerate(line):
                pattern[(x, y)] = 1 if c == '#' else 0
        patterns.append((pattern, x + 1, y + 1))
    return patterns

def solver(patterns):
    old = new = 0
    for pattern, w, h in patterns:
        scores = list()

        for p in range(1, w):
            to_check = {(x, y) for (x, y) in pattern.keys() if x < p}
            score = sum(pattern[(x, y)] == pattern.get((p + (p - x) - 1, y), pattern[(x, y)]) for x, y in to_check)
            scores.append((len(to_check) - score, p))

        for p in range(1, h):
            to_check = {(x, y) for (x, y) in pattern.keys() if y < p}
            score = sum(pattern[(x, y)] == pattern.get((x, p + (p - y) - 1), pattern[(x, y)]) for x, y in to_check)
            scores.append((len(to_check) - score, 100 * p))
        scores.sort()
        
        old += scores[0][1]
        new += scores[1][1]
    yield old
    yield new