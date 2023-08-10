from collections import deque
from pythonfw.ship_computer import Program
from pythonfw.classes       import Point
from pythonfw.functions     import bfs

def preprocessing(input: str) -> list[int]:
    return tuple(map(int, input.split(',')))

def solver(intcode): 
    maze, (pos, distance) = intcode_bfs(intcode)
    yield distance
    yield max(bfs(maze, pos, pt) for pt in maze)
            
                
def intcode_bfs(intcode: tuple[int]) -> set[tuple[int, int]]:
    x, y = 0, 0
    prog = Program(intcode)
    
    dx = {3: -1, 4: 1}
    dy = {1: -1, 2: 1}
    
    queue = deque([[(0, 0, intcode)]])
    maze = set((0, 0))
    
    while queue:
        path = queue.popleft()
        x, y, intcode = path[-1]
        prog = Program(intcode)
        for move, (x2, y2) in enumerate(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)), 1):
            temp = Program(prog.get_memory())
            if (x2, y2) not in maze:
                if (n:= temp.run(move)):
                    if n == 2: oxygen = ((x2, y2), len(path))
                    queue.append(path + [(x2, y2, temp.get_memory())])
                    maze.add((x2, y2))
    return maze, oxygen

