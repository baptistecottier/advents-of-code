import collections ; 

def bfs(maze, start , end):
    width , height = len(maze[0]) , len(maze)
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x , y) == end:
            return len(path)-1
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and maze[y2][x2] - maze[y][x] < 2 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
                
def generator(input) :
    grid = []
    starting_points = []
    for y , line in enumerate(input.splitlines()):
        grid_line =[]
        for x, c in enumerate(line) :
            match c : 
                case 'a' : 
                    grid_line.append(1)
                    starting_points.append((x,y))
                case 'S' : 
                    grid_line.append(0)
                    start = (x ,y)
                case 'E' :
                    grid_line.append(27)
                    end = (x,y)
                case _ : grid_line.append(ord(c)-ord('a')+1)
        grid.append(grid_line)
    return [grid, start, end, starting_points]
    
def part_1(input) :
    return bfs(input[0] , input[1], input[2])
    
    
def part_2(input) : 
    return min([item for item in [bfs(input[0] ,start, input[2]) for start in input[3]] if item != None]) 