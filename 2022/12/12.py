from collections        import defaultdict
from pythonfw.functions import bfs

                
def climbable(pos, new, heightmap):   
    return new in heightmap and (heightmap[new] - heightmap[pos]) < 2    
    
def preprocessing(input):
    grid = defaultdict(int)
    starting_points = []
    for y , line in enumerate(input.splitlines()):
        grid_line =[]
        for x, c in enumerate(line):
            match c: 
                case 'a': 
                    grid[(x, y)] = 1
                    starting_points.append((x,y))
                case 'S': 
                    grid[(x, y)] = 0
                    start = (x ,y)
                case 'E':
                    grid[(x, y)] = 27
                    end = (x,y)
                case _: grid[(x, y)] = ord(c) - ord('a') + 1
    return dict(grid), start, end, starting_points

def solver(heightmap):
    maze, start, end, starting_points = heightmap
    
    yield bfs(maze , start, end, predicate = climbable)
    yield min(dist for dist in (bfs(maze, start, end, predicate = climbable) for start in starting_points) if dist != -1) 