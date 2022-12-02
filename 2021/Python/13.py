with open("Day13/input") as f:
    content=f.read().splitlines()
    dots = content[:content.index('')]
    dots=[[int(item.split(',')[0]) , int(item.split(',')[1])] for item in dots]
    instructions=content[content.index('')+1:]
    max_x = max([item[0] for item in dots])
    max_y = max([item[1] for item in dots])
    grid = [[0 for x in range(max_x+1)] for y in range(max_y+1)]
    for dot in dots : grid[dot[1]][dot[0]]=1
    instructions=[[(item.split(' ')[-1]).split('=')[0] , int((item.split(' ')[-1]).split('=')[1])] for item in instructions]
    
    for axe , n in instructions :
        if axe=='x' :
            for xn in range(1,len(grid[0])-n) : 
                for yn in range(len(grid)) :
                    grid[yn][n-xn]=int(not ((not grid[yn][n-xn]) and (not grid[yn][n+xn])))
            grid=[[grid[y][x] for x in range(n)] for y in range(len(grid))]
    
        if axe=='y' :
            for xn in range(len(grid[0])) : 
                for yn in range(1,len(grid)-n) :
                    grid[n-yn][xn]=int(not ((not grid[n-yn][xn]) and (not grid[n+yn][xn])))
            grid=[[grid[y][x] for x in range(len(grid[0]))] for y in range(n)]

    for i in range(len(grid)) : 
        for j in range(len(grid[0])) :
            if grid[i][j]==0 : grid[i][j]='.'
            if grid[i][j]==1 : grid[i][j]='#'
        print(grid[i])
