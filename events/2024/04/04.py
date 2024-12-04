def preprocessing(puzzle_input):
    letters = {'X': set(), 'M': set(), 'A': set(), 'S': set()}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            letters[c].add((x, y))
    return letters

def solver(letters):
    yield find_xmas(letters)
    yield find_x_mas(letters)
    
def find_xmas(letters):
    cnt = 0
    for (x, y) in letters['X']:
        if (x - 1, y+1) in letters['M'] and (x - 2, y+2) in letters['A'] and (x - 3, y+3) in letters['S']: cnt += 1
        if (x - 1, y) in letters['M'] and (x - 2, y) in letters['A'] and (x - 3, y) in letters['S']: cnt += 1 # a gauche 
        if (x - 1, y-1) in letters['M'] and (x - 2, y-2) in letters['A'] and (x -3, y-3) in letters['S']: cnt += 1 #
        if (x, y+1) in letters['M'] and (x, y+2) in letters['A'] and (x, y+3) in letters['S']: cnt += 1
        if (x, y-1) in letters['M'] and (x, y-2) in letters['A'] and (x, y-3) in letters['S']: cnt += 1
        if (x + 1, y+1) in letters['M'] and (x + 2, y+2) in letters['A'] and (x + 3, y+3) in letters['S']: cnt += 1 # en bas à droite
        if (x + 1, y) in letters['M'] and (x + 2, y) in letters['A'] and (x + 3, y) in letters['S']: cnt += 1 # a droite
        if (x + 1, y-1) in letters['M'] and (x + 2, y-2) in letters['A'] and (x + 3, y-3) in letters['S']: cnt += 1
    return cnt

def find_x_mas(letters):
    cnt = 0
    for (x, y) in letters['A']:
        if (x-1, y-1) in letters['M'] and (x+1, y-1) in letters['M'] and (x+1, y+1) in letters['S'] and (x-1, y+1) in letters['S']: cnt +=1
        elif (x-1, y-1) in letters['M'] and (x-1, y+1) in letters['M'] and (x+1, y-1) in letters['S'] and (x+1, y+1) in letters['S']: cnt +=1
        elif (x+1, y-1) in letters['M'] and (x+1, y+1) in letters['M'] and (x-1, y-1) in letters['S'] and (x-1, y+1) in letters['S']: cnt +=1
        elif (x-1, y+1) in letters['M'] and (x+1, y+1) in letters['M'] and (x+1, y-1) in letters['S'] and (x-1, y-1) in letters['S']: cnt +=1
    return cnt
