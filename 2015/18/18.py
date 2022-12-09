with open("Day18/input") as f:
    temp_grid=[list(item.replace('#','1').replace('.','0')) for item in f.read().splitlines()]

    grid=[[0 for x in range(len(temp_grid)+2)] for y in range(len(temp_grid)+2)]
    for i in range(1,len(temp_grid)+1):
        grid[i][1:-1]=[int(x) for x in temp_grid[i-1]]
    grid[1][1]=1
    grid[1][-2]=1
    grid[-2][1]=1
    grid[-2][-2]=1
    for step in range(100):
        temp=[[0 for x in range(len(temp_grid)+2)] for y in range(len(temp_grid)+2)]
        for i in range(1,len(grid)-1):
            print(grid[i][1:-1])
        for x in range(1,len(grid)-1):
            for y in range(1,len(grid)-1):
                n=sum(grid[x-1][y-1:y+2])+grid[x][y-1]+grid[x][y+1]+sum(grid[x+1][y-1:y+2])
                if grid[x][y]==1 and n not in [2,3] : 
                    temp[x][y]=0
                elif grid[x][y]==0 and n==3 : temp[x][y]=1
                else : temp[x][y]=grid[x][y]
        temp[1][1]=1
        temp[1][-2]=1
        temp[-2][1]=1
        temp[-2][-2]=1
        grid=temp

        print('\n')
    print(sum(sum(grid[x]) for x in range(len(grid))))
            

