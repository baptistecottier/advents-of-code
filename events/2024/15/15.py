def preprocessing(puzzle_input):
    """
    During preprocessing, puzzle input is split such that we have the warehouse map
    and the moves the robot will do. We then extract walls, boxes and the rebot from
    the warehouse. For each move we associate the arrow with the corresponding 
    directions (dx, dy).
    """
    warehouse, raw_moves = puzzle_input.split('\n\n')
    walls = set()
    boxes = set()
    for y, line in enumerate(warehouse.splitlines()):
        for x, c in enumerate(line):
            match c:
                case '#': walls.add((x, y))
                case 'O': boxes.add((x, y))
                case '@': rx, ry = (x, y)
                case _ : pass

    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    moves = [directions[c] for c in raw_moves.replace("\n","")]
    return moves, walls, boxes, rx, ry


def solver(moves, walls, boxes, rx, ry):
    """
    Not a lot to say here. For each part we generate the appropriate data, then
    simulate the moves and return the sum of the coordinates of the boxes.
    """
    moved_small_boxes = move_small_boxes(moves, rx, ry, walls.copy(), boxes.copy())
    yield sum([100 * y + x for (x, y) in moved_small_boxes])
    
    moved_big_boxes = move_big_boxes(
        moves,
        (2 * rx, ry),
        {(2 * x, y) for (x, y) in walls}.union({(2 * x + 1, y) for (x, y) in walls}),
        {(2 * x, y) for (x, y) in boxes})
    yield sum([100 * y + x for (x, y) in moved_big_boxes])
    
    
def move_small_boxes(moves, rx, ry, walls, boxes):
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
    for dx, dy in moves:
        x, y = rx, ry
        if (x + dx, y + dy) in walls: 
            continue
        elif (x + dx, y + dy) not in boxes: 
            rx, ry = rx + dx, ry + dy
        else:
            while (x:= x + dx, y := y + dy) in boxes:
                pass
            if (x, y) not in walls: 
                boxes.remove((rx := rx + dx, ry:= ry + dy))
                boxes.add((x, y))
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
            continue
        elif dy == 0 and (x + delta, y + dy) not in boxes:
            x += dx
        elif dy != 0 and (x - 1, y + dy) not in boxes and (x, y + dy) not in boxes:
            y += dy
        elif dx: 
            boxes, x, y = move_horizontally(x, y, dx, boxes, walls)
        else:
            boxes, x, y = move_vertically(x, y, dy, boxes, walls)
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
    if (x + dx * i + delta, y) not in walls:
        for k in range(x + dx - delta, x + (i - delta) * dx, 2 * dx):
            boxes.remove((k, y))
            boxes.add((k + dx, y))
        x += dx
    return boxes, x, y


def move_vertically(x, y, dy, boxes: set, walls):
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
    span = set([(x - delta, y + dy)])
    to_move = set([(x - delta, y + dy)])

    while span:
        tx, ty = span.pop()
        for kx in (-1, 0, 1):
            if kx != -1 and (tx + kx, ty + dy) in walls:
                return boxes, x, y
            if (tx + kx, ty + dy) in boxes:
                to_move.add((tx + kx, ty + dy))
                span.add((tx + kx, ty + dy))
                
    boxes.difference_update(to_move)
    boxes.update({(tx, ty + dy) for (tx, ty) in to_move})
    return boxes, x, y + dy