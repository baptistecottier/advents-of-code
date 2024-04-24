from collections        import defaultdict
from pythonfw.functions import bfs


def preprocessing(puzzle_input):
    grid = defaultdict(int)
    starting_points = []

    for y , line in enumerate(puzzle_input.splitlines()):
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


def solver(maze, start, end, starting_points):
    min_dist = bfs(maze , start, end, predicate = climbable)
    yield min_dist
    
    for start in starting_points:
        dist = bfs(maze , start, end, predicate = climbable)
        if dist != -1 and dist < min_dist: 
            min_dist = dist

    yield min_dist


def climbable(pos, new, heightmap):   
    return new in heightmap and (heightmap[new] - heightmap[pos]) < 2    