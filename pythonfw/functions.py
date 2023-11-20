from operator import gt
from re           import findall
from collections  import defaultdict, deque
from math         import prod

import _md5

def bfs(maze, start, end, max_length = 1_000, predicate = None):
    if predicate == None:
        def predicate(pos, new, maze): return new in maze
    
    queue = deque([[start]])
    seen = set([start])
    
    while queue:
        path = queue.popleft()
        if len(path) > 1 + max_length: return -1
        x, y = path[-1]
        if (x, y) == end:
            return len(path)-1
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) not in seen and predicate((x, y), (x2, y2), maze):
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return -1
                
def chinese_remainder(equations, get_modulo = False):
    sum     = 0
    product = prod(modulo for _, modulo in equations)
    for remainder, modulo in equations:
        sub_product = product // modulo
        sum        += remainder * pow(sub_product, -1, modulo) * sub_product
    if get_modulo: return (sum % product, product)
    else: return sum % product

def dijkstra(map_dict, end_coords):
    unvisited = set(map_dict.keys())
    node_dict = {(0, 0): 0}
    current_node = (0, 0)
    
    while current_node != end_coords:
        x, y = current_node
        risk = node_dict[current_node]
        
        for next_to in [item for item in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if item in unvisited]:
            
            current_risk = node_dict.get(next_to, None)
            new_risk = risk + map_dict[next_to]
            if not current_risk or new_risk < current_risk:
                node_dict[next_to] = new_risk

        unvisited.remove(current_node)
        del node_dict[current_node]

        lowest_risk = min(node_dict.values())
        for coords, risk in node_dict.items():
            if risk == lowest_risk:
                current_node = coords
                break

    return node_dict[end_coords]

def extract_chunks(data: str, take: int, skip: int = 0, neg = True, func = lambda x: x):
    numbers = list(int(n) for n in findall(r'[-]?[0-9]+' if neg else r'[0-9]+', data))
    return list(func(numbers[i: i + take]) for i in range(0, len(numbers), take + skip))

def manhattan(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return abs(x1 - x2) + abs(y1 - y2)

def md5(to_hash: str) -> str:
    return _md5.md5(to_hash.encode()).hexdigest()

def screen_reader(screen: set) -> str:
    lx, ly = zip(*screen)
    mx = min(lx)
    my = min(ly)
    h = max(ly) - min(ly) + 1
    W = {6: 5, 10: 8}
    w = W[h]
    screen = {(x - mx, y - my) for (x, y) in screen}
    word = ''
    letters = [[] for _ in range(1 + max(x for (x, y) in screen) // w)]
    for (x, y) in screen:
        letters[x // w].append((x % w, y))
    for letter in letters:
        word += coords_to_letter(letter, w, h)
    return word

def coords_to_letter(coords, w, h):
    if h == 6:
        match len(coords):
            case 9: # J, L, Y
                if any(x == w - 1 for (x, y) in coords): return 'Y'
                elif all((0, y) in coords for y in range(h)): return 'L'
                else: return 'J'
            case 10: # C
                return 'C'
            case 11: # F, S
                if all((0, y) in coords for y in range(6)): return 'F'
                else: return 'S'
            case 12: # K, O, P, U, Z
                if all((x, 0) in coords for x in range(4)): return 'Z'
                elif all((3 - y, y) in coords for y in range(4)): return 'K'
                elif all((0, y) in coords for y in range(6)): return 'P'
                elif all((0, y) in coords for y in range(5)): return 'U'
                else: return 'O'
            case 13: # G
                return 'G'
            case 14: # A, E, H, R
                if all((3, y) in coords for y in range(6)): return 'H'
                elif all((x, x + 2) in coords for x in range(4)): return 'R'
                elif all((0, y) in coords for y in range(6)): return 'E'
                else: return 'A'
            case 15: # B
                return 'B'
        
    elif h == 10:
        match len(coords):
            case 15: return 'L'
            case 16: return 'J'
            case 18: return 'C'
            case 21: return 'P'
            case 19: return 'F'
            case 20: 
                if (0, 1) not in coords: return 'Z'
                elif (0, 2) in coords: return 'K'
                else: return 'X'
            case 24: # E, H
                if (1, 5) in coords: return 'A'
                if (0, 0) not in coords: return 'G'
                elif (1, 0) in coords: return 'E'
                else: return 'H'
                
            case 26: return 'R'
            case 28: return 'N'
            case 29: return 'B'
            
def sign(a, b = 0, f = gt) -> int: 
        if f(b, a): return -1
        if f(a, b): return 1
        return 0
    
    
### HELPER FOR OCR

## h = 6
# A: [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 3), (2, 0), (2, 3), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]
# B: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 2), (1, 5), (2, 0), (2, 2), (2, 5), (3, 1), (3, 3), (3, 4)]
# C: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (2, 0), (2, 5), (3, 1), (3, 4)]
# D: Not encountered yet
# E: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 2), (1, 5), (2, 0), (2, 2), (2, 5), (3, 0), (3, 5)]
# F: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0)]
# G: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (2, 0), (2, 3), (2, 5), (3, 1), (3, 3), (3, 4), (3, 5)]
# H: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]
# I: [(1, 0), (1, 5), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 0), (3, 5)]
# J: [(0, 4), (1, 5), (2, 0), (2, 5), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
# K: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (2, 1), (2, 3), (2, 4), (3, 0), (3, 5)]
# L: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5)]
# M: Not encountered yet
# N: Not encountered yet
# O: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (2, 0), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4)]
# P: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 3), (2, 0), (2, 3), (3, 1), (3, 2)]
# Q: Not encountered yet
# R: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 3), (2, 0), (2, 3), (2, 4), (3, 1), (3, 2), (3, 5)]
# S: [(0, 1), (0, 2), (0, 5), (1, 0), (1, 3), (1, 5), (2, 0), (2, 3), (2, 5), (3, 0), (3, 4)]
# T: Not encountered yet
# U: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (2, 5), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
# V: Not encountered yet
# W: Not encountered yet
# X: Not encountered yet
# Y: [(2, 5), (0, 1), (2, 4), (1, 2), (0, 0), (3, 2), (4, 1), (2, 3), (4, 0)]
# Z: [(0, 0), (0, 4), (0, 5), (1, 0), (1, 3), (1, 5), (2, 0), (2, 2), (2, 5), (3, 0), (3, 1), (3, 5)]

## h = 10
# A: (24, [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 1), (1, 5), (2, 0), (2, 5), (3, 0), (3, 5), (4, 1), (4, 5), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9)])
# B: (29, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 4), (1, 9), (2, 0), (2, 4), (2, 9), (3, 0), (3, 4), (3, 9), (4, 0), (4, 4), (4, 9), (5, 1), (5, 2), (5, 3), (5, 5), (5, 6), (5, 7), (5, 8)])
# C: (18, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 9), (2, 0), (2, 9), (3, 0), (3, 9), (4, 0), (4, 9), (5, 1), (5, 8)])
# D: Not encountered yet
# E: (24, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 4), (1, 9), (2, 0), (2, 4), (2, 9), (3, 0), (3, 4), (3, 9), (4, 0), (4, 4), (4, 9), (5, 0), (5, 9)])
# F: (19, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 4), (2, 0), (2, 4), (3, 0), (3, 4), (4, 0), (4, 4), (5, 0)])
# G: (24, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 9), (2, 0), (2, 9), (3, 0), (3, 5), (3, 9), (4, 0), (4, 5), (4, 8), (5, 1), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9)])
# H: (24, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 4), (2, 4), (3, 4), (4, 4), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9)])
# I: Not encountered yet
# J: (16, [(0, 7), (0, 8), (1, 9), (2, 9), (3, 0), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (5, 0)])
# K: (20, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 4), (1, 5), (2, 3), (2, 6), (3, 2), (3, 7), (4, 1), (4, 8), (5, 0), (5, 9)])
# L: (15, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)])
# M: Not encountered yet
# N: (28, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (3, 6), (4, 7), (4, 8), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9)])
# O: Not encountered yet
# P: (21, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 4), (2, 0), (2, 4), (3, 0), (3, 4), (4, 0), (4, 4), (5, 1), (5, 2), (5, 3)])
# Q: Not encountered yet
# R: (26, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 4), (2, 0), (2, 4), (3, 0), (3, 4), (3, 5), (4, 0), (4, 4), (4, 6), (4, 7), (5, 1), (5, 2), (5, 3), (5, 8), (5, 9)])
# S: Not encountered yet
# T: Not encountered yet
# U: Not encountered yet
# V: Not encountered yet
# W: Not encountered yet
# X: (20, [(0, 0), (0, 1), (0, 8), (0, 9), (1, 2), (1, 3), (1, 6), (1, 7), (2, 4), (2, 5), (3, 4), (3, 5), (4, 2), (4, 3), (4, 6), (4, 7), (5, 0), (5, 1), (5, 8), (5, 9)])
# Y: Not encountered yet
# Z: (20, [(0, 0), (0, 7), (0, 8), (0, 9), (1, 0), (1, 6), (1, 9), (2, 0), (2, 5), (2, 9), (3, 0), (3, 4), (3, 9), (4, 0), (4, 3), (4, 9), (5, 0), (5, 1), (5, 2), (5, 9)])