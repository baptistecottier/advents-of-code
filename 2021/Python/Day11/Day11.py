with open("input") as f:
    input=[[int(item) for item in list(line)] for line in f.read().splitlines()]
    grid=[[100 for x in range(len(input[0])+2)] for y in range(len(input)+2)]
    for i in range(len(input)):
        grid[i+1][1:-1]=input[i]

def is_tens(grid):
    if any([grid[x][y]>9 for x in range(1,len(grid)-1) for y in range(1,len(grid[0])-1)]): return 1
    else : return 0

count_flashed=0
flashed=[]
round=1
while(len(flashed)!= 100):
    flashed=[]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y]+=1
    while (is_tens(grid)!=0):
        for x in range(1,len(grid)-1):
            for y in range(1,len(grid[0])-1):
                if grid[x][y]>9 and [x,y] not in flashed :
                    flashed.append([x,y])
                    count_flashed+=1
                    grid[x][y]=-1000000
                    for a , b in [[x-1,y],[x+1,y],[x,y-1],[x,y+1],[x-1,y-1],[x-1,y+1],[x+1, y-1],[x+1, y+1]]:
                        grid[a][b]+=1
    for a , b in flashed : grid[a][b]=0
    round+=1
print(round)
