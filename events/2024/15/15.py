from collections import deque

def preprocessing(puzzle_input):
    warehouse, raw_moves = puzzle_input.split('\n\n')
    moves = list()
    for c in raw_moves:
        match c :
            case '^': moves.append((0, -1))
            case '>': moves.append((1, 0))
            case 'v': moves.append((0, 1))
            case '<': moves.append((-1, 0))
            case _: pass

    return warehouse, moves

def warehouse_to_data(warehouse, extra_width = False):
    if extra_width:
        warehouse = warehouse.replace('#' ,"##").replace('O' ,"[]").replace('.' ,"..").replace('@' ,"@.")
    walls = set()
    boxes = set()
    for y, line in enumerate(warehouse.splitlines()):
        for x, c in enumerate(line):
            match c:
                case '#': walls.add((x, y))
                case '[': boxes.add((x, y))
                case 'O': boxes.add((x, y))
                case '@': robot = (x, y)
                case _ : pass
    return walls, boxes, robot, x, y
    
def solver(raw_warehouse, moves):
    walls, boxes, robot, mx, my = warehouse_to_data(raw_warehouse)
    x, y = robot
    
    for dx, dy in moves:
        if (x + dx, y + dy) in walls:
            pass
        elif (x + dx, y + dy) in boxes:
            boxes.remove((x + dx, y + dy))
            i = 2
            while (x + i * dx, y + i * dy) in boxes:
                i += 1
                if (x + i * dx, y + i * dy) in walls:
                    i = 1
                    break
            if (x + i * dx, y + i * dy) in walls:
                i = 1
            boxes.add((x + i * dx, y + i * dy))
            x += (i > 1) * dx
            y += (i > 1) * dy
        else:
            x += dx
            y += dy
    yield sum([100 * y + x for (x, y) in boxes])
    
    def print_warehouse():
        for ty in range(my + 1):
            line = ""
            left = False
            for tx in range(mx + 1):
                if left: 
                    line += ']'
                    left = False
                else:
                    if (tx, ty) in walls : line += '#'
                    elif (tx, ty) == (x, y): line += '@'
                    elif (tx, ty) in boxes: 
                        line += "["
                        left = True
                    else : line += '.'
            print(line)
        print()

        
    walls, boxes, robot, mx, my = warehouse_to_data(raw_warehouse, True)
    x, y = robot
    
    for dx, dy in moves:
        delta = -2 if dx == -1 else dx
        if (x + dx, y + dy) in walls:
            pass
        elif dy == 0 and (x + delta, y + dy) not in boxes:
            x += dx
            y += dy
        elif dy == 1 and (x - 1, y + 1) not in boxes and (x, y + 1) not in boxes:
            y += dy
        elif dy == -1 and (x - 1, y - 1) not in boxes and (x, y - 1) not in boxes:
            y += dy
        else :
            match (dx, dy):
                case (1 , 0):
                    i = 3
                    while (x + i, y) in boxes:
                        i += 2
                    if (x + i, y) in walls:
                        pass
                    else:
                        for k in range(x + 1, x + i, 2):
                            boxes.remove((k, y))
                            boxes.add((k + 1, y))
                        x += 1
                case (-1, 0):
                        i = 4
                        while (x + i * dx, y) in boxes:
                            i += 2
                        if (x + (i - 1) * dx, y) in walls:
                            pass
                        else:
                            for k in range(x - 2, x + (i - 1) * dx, -2):
                                boxes.remove((k, y))
                                boxes.add((k - 1, y))
                            x += dx
                case (0 , 1): 
                    if (x - 1, y + 1) in boxes:
                        span = deque([(x - 1, y + 1)])
                        to_move = deque([(x - 1, y + 1)])
                    else:
                        span = deque([(x, y + 1)])
                        to_move = deque([(x, y + 1)])
                    while span:
                        tx, ty = span.popleft()
                        if (tx, ty + 1) in boxes:
                            to_move.append((tx, ty + 1))
                            span.append((tx, ty + 1))
                        if (tx - 1, ty + 1) in boxes:
                            to_move.append((tx - 1, ty + 1))
                            span.append((tx - 1, ty + 1))
                        if (tx + 1, ty + 1) in boxes:
                            to_move.append((tx + 1, ty + 1))
                            span.append((tx + 1, ty + 1))
                    # print(to_move, ty)
                    if all(((xx, yy + 1) not in walls for (xx, yy) in to_move)) and \
                       all(((xx + 1, yy + 1) not in walls for (xx, yy) in to_move)): 
                        while to_move:
                            tx, ty = to_move.pop()
                            try:
                                boxes.remove((tx, ty))
                            except:
                                pass
                            boxes.add((tx, ty + 1))
                        y += 1
                case (0, -1):
                    if (x - 1, y - 1) in boxes:
                        span = deque([(x - 1, y - 1)])
                        to_move = deque([(x - 1, y - 1)])
                    else:
                        span = deque([(x, y - 1)])
                        to_move = deque([(x, y - 1)])
                    while span:
                        tx, ty = span.popleft()
                        if (tx, ty - 1) in boxes:
                            to_move.append((tx, ty - 1))
                            span.append((tx, ty - 1))
                        if (tx - 1, ty - 1) in boxes:
                            to_move.append((tx - 1, ty - 1))
                            span.append((tx - 1, ty - 1))
                        if (tx + 1, ty - 1) in boxes:
                            to_move.append((tx + 1, ty - 1))
                            span.append((tx + 1, ty - 1))
                    if all(((xx, yy - 1) not in walls for (xx, yy) in to_move)) and \
                       all(((xx + 1, yy - 1) not in walls for (xx, yy) in to_move)):                         
                        while to_move:
                            tx, ty = to_move.pop()
                            try:
                                boxes.remove((tx, ty))
                            except:
                                pass
                            boxes.add((tx, ty - 1))
                        y -= 1
    yield sum([100 * y + x for (x, y) in boxes])