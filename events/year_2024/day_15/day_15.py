"""
Advent of Code - Year 2024 - Day 15
https://adventofcode.com/2024/day/15
"""


from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> tuple[
        list[tuple[int, int]],
        set[tuple[int, int]],
        set[tuple[int, int]],
        int,
        int]:
    """
    Parses the puzzle input into moves, wall positions, box positions, and the robot's coordinates.
    """
    warehouse, raw_moves = puzzle_input.split('\n\n')
    walls = set()
    boxes = set()
    rx = ry = -1
    for y, line in enumerate(warehouse.splitlines()):
        for x, c in enumerate(line):
            match c:
                case '#': walls.add((x, y))
                case 'O': boxes.add((x, y))
                case '@': rx, ry = (x, y)
                case _: pass

    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    moves = [directions[c] for c in raw_moves.replace("\n", "")]
    return moves, walls, boxes, rx, ry


def solver(
        moves: list[tuple[int, int]],
        walls: set[tuple[int, int]],
        boxes: set[tuple[int, int]],
        rx: int,
        ry: int
        ) -> Iterator[int]:
    """
    Not a lot to say here. For each part we generate the appropriate data, then
    simulate the moves and return the sum of the coordinates of the boxes.
    """
    moved_small_boxes = move_small_boxes(moves, rx, ry, walls.copy(), boxes.copy())
    moved_big_boxes = move_big_boxes(
        moves,
        (2 * rx, ry),
        {(2 * x, y) for (x, y) in walls}.union({(2 * x + 1, y) for (x, y) in walls}),
        {(2 * x, y) for (x, y) in boxes})

    for moved_boxes in (moved_small_boxes, moved_big_boxes):
        yield sum(100 * y + x for (x, y) in moved_boxes)


def move_small_boxes(
        moves: list[tuple[int, int]],
        rx: int,
        ry: int,
        walls: set[tuple[int, int]],
        boxes: set[tuple[int, int]]
        ) -> set[tuple[int, int]]:
    """
    Moves small boxes on a grid according to the given moves, updating their positions while
    considering walls and other boxes.
    """
    for dx, dy in moves:
        x, y = rx, ry
        if (x + dx, y + dy) in walls:
            continue
        if (x + dx, y + dy) not in boxes:
            rx, ry = rx + dx, ry + dy
        else:
            while (x := x + dx, y := y + dy) in boxes:
                pass
            if (x, y) not in walls:
                boxes.remove((rx := rx + dx, ry := ry + dy))
                boxes.add((x, y))
    return boxes


def move_big_boxes(
        moves: list[tuple[int, int]],
        robot: tuple[int, int],
        walls: set[tuple[int, int]],
        boxes: set[tuple[int, int]]
        ) -> set[tuple[int, int]]:
    """
    Simulation of the moves made by the robot in warehouse with big boxes. For each move direction
    we check if the move leads to a wall or a box. If a box is met, the boxes moves will depend if
    the move is made horizontally or vertically.
    """
    x, y = robot
    for dx, dy in moves:
        delta = -2 if dx == -1 else dx
        if (x + dx, y + dy) in walls:
            continue
        if dy == 0 and (x + delta, y + dy) not in boxes:
            x += dx
        elif dy != 0 and (x - 1, y + dy) not in boxes and (x, y + dy) not in boxes:
            y += dy
        elif dx:
            boxes, x, y = move_horizontally(x, y, dx, boxes, walls)
        else:
            boxes, x, y = move_vertically(x, y, dy, boxes, walls)
    return boxes


def move_horizontally(
        x: int,
        y: int,
        dx: int,
        boxes: set[tuple[int, int]],
        walls: set[tuple[int, int]]
        ) -> tuple[set[tuple[int, int]], int, int]:
    """
    Moves boxes horizontally along the x-axis if possible, updating their positions and returning
    the new state.
    """
    delta = dx == -1
    i = 3 + delta
    while (x + dx * i, y) in boxes:
        i += 2
    if (x + dx * i + delta, y) not in walls:
        for k in range(x + dx - delta, x + (i - delta) * dx, 2 * dx):
            boxes.remove((k, y))
            boxes.add((k + dx, y))
        x += dx
    return boxes, x, y


def move_vertically(
        x: int,
        y: int,
        dy: int,
        boxes: set[tuple[int, int]],
        walls: set[tuple[int, int]]
        ) -> tuple[set[tuple[int, int]], int, int]:
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
