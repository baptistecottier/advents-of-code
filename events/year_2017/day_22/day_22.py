"""Advent of Code - Year 2017 - Day 22"""

def preprocessing(puzzle_input: str) -> tuple[list[tuple[int, int]], int]:
    """
    Parse the puzzle input into a set of infected nodes and determine grid size.
    
    Args:
        puzzle_input (str): The puzzle input as a string, representing a grid.
        
    Returns:
        tuple: A pair containing:
            - list of tuples: Coordinates (x, y) of infected nodes
            - int: Size of the grid
    """
    infected = []
    grid = puzzle_input.splitlines()
    size = len(grid)
    for y, line in enumerate(grid[::-1]):
        for x, c in enumerate(line):
            if c == '#':
                infected.append((x, y))
    return infected, size


def solver(infected: list[tuple[int, int]], size: int):
    """
    Solves the virus infection problem for part 1 and part 2 using the burst function.
    """
    yield burst(infected, size, 1)
    yield burst(infected, size, 2)


def burst(infected: list[tuple[int, int]], size: int, bursts: int):
    """Simulate virus burst activity in a grid.
    
    The function simulates a virus carrier moving through a grid, infecting or cleaning nodes
    based on specific rules. The virus carrier can turn left, right, or reverse direction
    depending on the state of the current node.
    
    Args:
        infected: A collection of (x, y) coordinates representing initially infected nodes.
        size: The size of the initial grid containing infected nodes.
        bursts: Determines the number of possible states for each node and affects the
               total number of simulation steps (10^(1 + 3*bursts)).
    
    Returns:
        int: The count of nodes that became infected during the simulation.
    
    Note:
        - The grid is represented as a 2D array with states from 0 to 2*bursts-1.
        - The virus carrier starts at the center of the grid.
        - Direction changes depend on the current node's state.
    """
    half_grid_size = 400
    grid = [[0 for _ in range(2 * half_grid_size)] for _ in range(2 * half_grid_size)]

    for x, y in infected:
        iy = half_grid_size - (size // 2) + y
        ix = half_grid_size - (size // 2) + x
        grid[iy][ix] = bursts
    cx, cy = half_grid_size, half_grid_size
    dx, dy = 0, 1
    cnt = 0

    for _ in range(10 ** (1 + 3 * bursts)):
        grid[cy][cx] = (grid[cy][cx] + 1) % (2 * bursts)
        if grid[cy][cx] == bursts:
            cnt += 1

        if grid[cy][cx] == 3 * (bursts - 1):
            dx, dy = turn_right(dx, dy)
        elif grid[cy][cx] == 1:
            dx, dy = turn_left(dx, dy)
        elif grid[cy][cx] == 0:
            dx, dy = -dx, -dy

        cx += dx
        cy += dy
    return cnt


def turn_left(dx, dy):
    """
    Rotates the direction 90° to the left.
    """
    match dx, dy:
        case n, 0: return 0, n
        case 0, n: return -n, 0
        case _: raise ValueError("Invalid direction")


def turn_right(dx, dy):
    """
    Rotates the direction 90° to the right.
    """
    match dx, dy:
        case n, 0: return 0, -n
        case 0, n: return n, 0
        case _: raise ValueError("Invalid direction")
