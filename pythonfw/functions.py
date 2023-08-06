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
    letters = [[] for _ in range(10)]
    for (x, y) in screen:
        letters[x // w].append((x % w, y))
    for letter in letters:
        match len(letter):
            case 9: # J, L, Y
                if any(x == w - 1 for (x, y) in letter): word += 'Y'
                elif all((0, y) in letter for y in range(h)): word += 'L'
                else: word += 'J'
            case 10: # C
                word += 'C'
            case 11: # F, S
                if all((0, y) in letter for y in range(6)): word += 'F'
                else: word += 'S'
            case 12: # K, O, P, U, Z
                if all((x, 0) in letter for x in range(4)): word += 'Z'
                elif all( (3 - y, y) in letter for y in range(4)): word += 'K'
                elif all((0, y) in letter for y in range(6)): word += 'P'
                elif all((0, y) in letter for y in range(5)): word += 'U'
                else: word += 'O'
            case 13: # G
                word += 'G'
            case 14: # A, E, H, R
                if all((3, y) in letter for y in range(6)): word += 'H'
                elif all((x, x + 2) in letter for x in range(4)): word += 'R'
                elif all((0, y) in letter for y in range(6)): word += 'E'
                else: word += 'A'
            case 15: # B
                word += 'B'
    return word

def sign(a: int) -> int: 
        return (a > 0) - (0 > a)