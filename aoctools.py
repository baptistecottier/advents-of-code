from re           import findall
from collections  import defaultdict, deque
from math         import prod

class Register(dict):
    def __init__(self, *args):
        super().__init__(*args)
    def get(self, item):
        if item in self:
            return self.__getitem__(item)
        else:
            return int(item)
        
class Point():
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    def manhattan(self, x = 0, y = 0):
        return abs(self.x - x) + abs(self.y - y)
    def xy(self):
        return (self.x, self.y)
    def move(self, x = 0, y = 0):
        self.x += x
        self.y += y


def bfs(maze, start, end, max_length = 1_000):
    queue = deque([[start]])
    seen = set([start])
    
    while queue:
        path = queue.popleft()
        if len(path) > 1 + max_length: return None
        x, y = path[-1]
        if (x, y) == end:
            return len(path)-1
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) in maze and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
                
def chinese_remainder(equations, get_modulo = False):
    sum     = 0
    product = prod(modulo for _, modulo in equations)
    for remainder, modulo in equations:
        sub_product = product // modulo
        sum        += remainder * pow(sub_product, -1, modulo) * sub_product
    if get_modulo: return (sum % product, product)
    else: return sum % product
    
def extract_chunks(data: str, take: int, skip: int = 0):
    numbers = tuple(int(n) for n in findall(r'[-]?[0-9]+', data))
    return tuple(numbers[i: i + take] for i in range(0, len(numbers), take + skip))

def manhattan(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return abs(x1 - x2) + abs(y1 - y2)

def screen_to_word(screen: set):
    word = ''
    letters = [[] for _ in range(10)]
    for (x, y) in screen:
        letters[x // 5].append((x % 5, y))
    for letter in letters:
        match len(letter):
            case 9: # J, L, Y
                if any(x == 4 for (x, y) in letter): word += 'Y'
                elif all((0, y) in letter for y in range(6)): word += 'L'
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

    