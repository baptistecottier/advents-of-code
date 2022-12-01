from AoC_tools import read_input

vents = read_input().splitlines()

coordinates=[vent.split(' -> ') for vent in vents]
grid=[[0 for x in range(1000)] for y in range(1000)]
for start,end in coordinates:
    start_y, start_x = [int(item) for item in start.split(',')]
    end_y, end_x = [int(item) for item in end.split(',')]
    if start_x==end_x:
        for y in range(min(end_y,start_y), max(end_y,start_y)+1): grid[start_x][y]+=1
    
    elif start_y==end_y:
        for x in range(min(end_x,start_x), max(end_x,start_x)+1): grid[x][start_y]+=1

    elif end_x > start_x:
        if end_y > start_y: #
            for step in range(end_y-start_y+1): grid[start_x+step][start_y+step]+=1
        elif end_y < start_y:
            for step in range(start_y-end_y+1): grid[start_x+step][start_y-step]+=1
    
    else :
        if end_y > start_y:
            for step in range(end_y-start_y+1): grid[end_x+step][end_y - step]+=1
        elif end_y < start_y:
            for step in range(start_y-end_y+1): grid[end_x+step][end_y+step]+=1

for x,y in list(zip(range(start_x, end_x+1), range(start_y, end_y+1))): print(x,y)

score=0
for n in range(1000000):
    if grid[n//1000][n%1000]>1 : score+=1
print(score)