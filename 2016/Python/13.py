import collections

width , height = 50 , 50

def bfs(maze, start , end):
    queue = collections.deque([[start]]) # Initialise the queue of paths at the start point
    visited = set([]) # Add the starting point to the visited locations

    while queue: 
        path = queue.popleft() # Extract the first path in the queue
        x, y = path[-1] # Location is the last coordonates of the path
        visited.add((x,y)) # Add the actual coordinates to the visited points
        if (x , y) == end: # Test if this is the ending point
            return len(path)-1 # If yes, return the length of the path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)): # If no, consider all the available neighbours
            if 0 <= x2 < width and 0 <= y2 < height and maze[y2][x2] != '#' and (x2, y2) not in visited:
                queue.append(path + [(x2, y2)]) # Create the new paths to the queue


print('I am at location (1,1) and want to reach location (31,39). Let\'s go !')
maze=[['.' for _ in range(width)] for _ in range(height)]
fav_number=1358

for x in range(width):
    v=x*(x+3)+fav_number
    for y in range(height):
        if bin(v).count('1') % 2 : maze[y][x]='#'
        v+=2*(x+y+1)

print('Here I am ! This took me' , bfs(maze, (1,1) , (31,39)), 'steps')


print('Hmmm... I wonder how many distinct location I can visit in at most 50 steps...')
cnt = sum([bfs(maze, (1,1) , (x,y)) != None and bfs(maze, (1,1) , (x,y)) <= 50  for x in range(50) for y in range(50)])
print('Only', cnt, '? I was expecting more...')
