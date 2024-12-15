from collections import deque

def preprocessing(puzzle_input):
    """
    During preprocessing, puzzle input is split such that we have the warehouse map
    and the moves the robot will do. For each move we associate the arrow with the
    corresponding directions (dx, dy).
    """
    warehouse, raw_moves = puzzle_input.split('\n\n')
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    moves = [directions[c] for c in raw_moves.replace("\n","")]
    return warehouse, moves


def solver(raw_warehouse, moves):
    """
    Not a lot to say here. For each part we generate the appropriate data, then
    simulate the moves and return the sum of the coordinates of the boxes.
    """
    walls, boxes, robot = warehouse_to_data(raw_warehouse)
    boxes = move_small_boxes(moves, robot, walls, boxes)
    yield sum([100 * y + x for (x, y) in boxes])
    
    walls, boxes, robot = warehouse_to_data(raw_warehouse, extra_width = True)
    boxes = move_big_boxes(moves, robot, walls, boxes)
    yield sum([100 * y + x for (x, y) in boxes])
    
    
def warehouse_to_data(warehouse, extra_width = False):
    """
    This function first apply the width extension if instructed so by doubling walls
    thickness and adding an empty space after each other element in the warehouse.
    NOTE: Replacing 'O' with 'O.' is enough as we will only look for left parts of 
    boxes in the resolution of the puzzle.
    
    Then the function transforms the warehouse to two sets and a pair (x, y) 
    corresponding to the position of the robot. A first set contains all the pieces
    of wall coordinates and the second one contains all the boxes.
    """
    if extra_width:
        warehouse = warehouse.replace('#' ,"##") \
                             .replace('.' ,"..") \
                             .replace('O' ,"O.") \
                             .replace('@' ,"@.")
    walls = set()
    boxes = set()
    for y, line in enumerate(warehouse.splitlines()):
        for x, c in enumerate(line):
            match c:
                case '#': walls.add((x, y))
                case 'O': boxes.add((x, y))
                case '@': robot = (x, y)
                case _ : pass
    return walls, boxes, robot
    
    
def move_small_boxes(moves, robot, walls, boxes):
    """
    Simulation of the moves made by the robot in warehouse with small boxes. For
    each move direction we check if the move leads to a wall or a box. If a box 
    is met, we remove that box from the set of boxes and try to place it after the
    last box in the same direction. If there is no such place, we reinsert the box
    at its original place.
    
                        An empty space is met, the box is add
                        to the set with its new coordinates
                                                  ↓
    case 1 (direction = (0, 1)) | .@OOO.# -> .@?OO.# -> ..@OOO# 
    case 2 (direction = (0, 1)) | O.@OOO# -> O.@?OO# -> O.@OOO#
                                                   ↑
                    A wall is met, we come back to initial position
                    and reinsert the box coordinate to the set
    """
    x, y = robot
    for dx, dy in moves:
        if (x + dx, y + dy) in walls: 
            pass
        elif (x + dx, y + dy) not in boxes:
            x, y = (x + dx, y + dy)
        else:
            boxes.remove((x + dx, y + dy))
            i = 2
            while (x + i * dx, y + i * dy) in boxes:
                i += 1
            if (x + i * dx, y + i * dy) in walls:
                i = 1
            boxes.add((x + i * dx, y + i * dy))
            # If the box is more than one step away (i > 1), the robot can move.
            x += (i > 1) * dx
            y += (i > 1) * dy
    return boxes


def move_big_boxes(moves, robot, walls, boxes):
    """
    Simulation of the moves made by the robot in warehouse with big boxes. For
    each move direction we check if the move leads to a wall or a box. If a box 
    is met, the boxes moves will depend if the move is made horizontally or 
    vertically.
    """
    x, y = robot 
    for dx, dy in moves:
        delta = -2 if dx == -1 else dx
        if (x + dx, y + dy) in walls:
            pass
        elif dy == 0 and (x + delta, y + dy) not in boxes:
            x += dx
        elif dy != 0 and (x - 1, y + dy) not in boxes and (x, y + dy) not in boxes:
            y += dy
        else :
            match (dx, dy):
                case (_ , 0): boxes, x, y = move_horizontally(x, y, dx, boxes, walls)
                case (0 , _): boxes, x, y = move_vertically(x, y, dy, boxes, walls)
    return boxes


def move_horizontally(x, y, dx, boxes, walls):
    """
    In the case of an horizontal move, all boxes are aligned, and the logic is the
    same as the prior case, except the step between boxes is 2. As boxes are shifted
    by one position, all boxes between the robot and the empty space are shifted by
    one step in the direction of the move.
    """
    delta = (dx == -1)
    i = 3 + delta
    while (x + dx * i, y) in boxes:
        i += 2
    if (x + dx * i + delta, y) in walls:
        pass
    else:
        for k in range(x + dx - delta, x + (i - delta) * dx, 2 * dx):
            boxes.remove((k, y))
            boxes.add((k + dx, y))
        x += dx
    return boxes, x, y


def move_vertically(x, y, dy, boxes, walls):
    """
    In the case of a vertical move, a single box can push several boxes. Hence, we
    need to check not only the position aligned with the box but also on the sides:
    
                                direction = (0, -1)
                    ......      ......      ......      ......
                    ..[]..      .[]...      .[][].      ...[].
                    ..[]..      ..[]..      ..[]..      ..[]..
                    ......      ......      ......      ......
                    
    The box finding process is applied recursively until an empty space or a wall is
    met. If a wall is met, the whole move is blocked, nothing happens. Otherwise,
    all boxes moves accordingly to the vertical direction. The function returns the
    updated (potentially unchanged) set of boxes and robot position.
    """
    delta = (x - 1, y + dy) in boxes
    span = deque([(x - delta, y + dy)])
    to_move = deque([(x - delta, y + dy)])

    while span:
        tx, ty = span.popleft()
        for kx in (0, 1):
            if (tx + kx, ty + dy) in walls:
                return boxes, x, y
            if (tx + kx, ty + dy) in boxes:
                to_move.appendleft((tx + kx, ty + dy))
                span.append((tx + kx, ty + dy))
        if (tx - 1, ty + dy) in boxes:
                to_move.appendleft((tx - 1, ty + dy))
                span.append((tx - 1, ty + dy))

    for tx, ty in to_move:
        try:
            boxes.remove((tx, ty))
            boxes.add((tx, ty + dy))
        except:
            pass
    y += dy
    return boxes, x, y