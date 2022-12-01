from itertools import permutations
from parse import parse
from AoC_tools import read_input, print_grid, manhattan_distance

nodes_infos=read_input().splitlines()[2:]

partI_grid=[]
grid = [['.' for _ in range(35)] for _ in range(29)]
for node in nodes_infos:
    x, y, size, used, avail, use=[int(item.replace(' ','')) for item in parse('/dev/grid/node-x{}-y{} {}T {}T {}T {}%',node)]
    partI_grid.append([size, used, avail, use])
    if used > 100 : 
        grid[y][x]='#'
    elif used==0 : 
        grid[y][x]='_'
        empty=(x,y)
grid[0][-1] = 'T'
grid[0][0] = 'G'

count=0
for A, B in permutations(partI_grid, 2):
    if A[1]!=0 and A != B and A[1]<B[2] : count += 1

print('There are:', count, 'viable pairs')

#Uncomment to display the grid
print_grid(grid)

for pos in range(len(grid)*len(grid[0])):
    y=pos//len(grid[0])
    x=pos%len(grid[0])
    if grid[y][x]=='#':
        try : 
            if grid[y][x-1]=='.': 
                wall=(x-1,y)
                break
        except : 
            if grid[y][x-1]=='.': 
                wall=(x+1,y)
                break


steps=manhattan_distance(empty , wall) # Bring the empty disk to the starting disk contourning the wall
steps+=manhattan_distance(wall,(len(grid[0])-1, 0)) 
steps+=5*(len(grid[0])-2) # 5 steps are needed for the empty space to contourner the targetted disk
print('Part II:' , steps)
