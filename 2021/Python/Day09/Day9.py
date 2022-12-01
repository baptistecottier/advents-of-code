with  open("input") as f:
    temp_grid=f.read().splitlines()
    grid=[[9 for x in range(len(temp_grid[0])+2)] for y in range(len(temp_grid)+2)]
    for i in range(1,len(temp_grid)+1):
        grid[i][1:-1]=[int(x) for x in temp_grid[i-1]]

risk=0
low_points=[]
for x in range(1,len(grid)-1):
        for y in range(1,len(grid[0])-1):
            if all(grid[x][y]<grid[a][b] for [a,b] in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]):            
                risk=risk+grid[x][y]+1
                low_points.append([x,y])

print("Part I :", risk)


def basin_size(grid, lp_x, lp_y, pt_done):
    if grid[lp_x][lp_y] != 9 and [lp_x,lp_y] not in pt_done :
            pt_done.append([lp_x,lp_y])
            return 1 + basin_size(grid, lp_x, lp_y-1, pt_done) + basin_size(grid, lp_x, lp_y+1, pt_done) + basin_size(grid, lp_x-1, lp_y, pt_done) + basin_size(grid, lp_x+1, lp_y, pt_done)
    else : return 0
 
sizes=[0,0,0]
for [lp_x, lp_y] in low_points:
    if basin_size(grid, lp_x, lp_y, [])>min(sizes):sizes[sizes.index(min(sizes))]=basin_size(grid, lp_x, lp_y, [])
print("Part II :", sizes[0]*sizes[1]*sizes[2])