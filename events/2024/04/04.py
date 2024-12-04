def preprocessing(puzzle_input):
    """
    Preprocessing consists in going through the puzzle input and stock position of the letters 'X', 'M', 'A' and 'S'.
    """
    letters = {'X': set(), 'M': set(), 'A': set(), 'S': set()}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            letters[c].add((x, y))
    return letters

def solver(letters):
    yield find_xmas(letters)
    yield find_x_mas(letters)
    
def find_xmas(letters):
    """
    Patterns to be detected are:
    XMAS    X...    X...    ...X    SAMX    S...    S...    ...S
    ....    .M..    M...    ..M.    ....    .A..    A...    ..A.
    ....    ..A.    A...    .A..    ....    ..M.    M...    .M..
    ....    ...S    S...    S...    ....    ...X    X...    X...
    This function starts from every detected 'X' then check if a "MAS" is formed in any of the possible directions
    """
    cnt = 0
    directions = {(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)}
    for (x, y) in letters['X']:
        cnt += sum((x +     dx, y +     dy) in letters['M'] and \
                   (x + 2 * dx, y + 2 * dy) in letters['A'] and \
                   (x + 3 * dx, y + 3 * dy) in letters['S'] for (dx, dy) in directions)
    return cnt

def find_x_mas(letters):
    """
    Patterns to be detected are:
    M.S     S.M     M.M     S.S
    .A.     .A.     .A.     .A.
    M.S     S.M     S.S     M.M
    
    Readind left-to-right, top-to-bottom without considering the 'A', the patterns are "MSMS", "SMSM", "MMSS" and "SSMM".
    This function therefore look for this patterns around all 'A'. 
    """
    cnt = 0
    for (x, y) in letters['A']:
        for (l1, l2, l3, l4) in ["MSMS", "SMSM", "MMSS", "SSMM"]:
            if ((x - 1, y - 1) in letters[l1] and (x + 1, y - 1) in letters[l2] and ((x - 1, y + 1) in letters[l3] and (x + 1, y + 1) in letters[l4])):
                cnt += 1
                break
    return cnt
