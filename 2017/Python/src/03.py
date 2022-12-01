from AoC_tools import print_grid

input = 361527
x = int((input - 1) ** 0.5 + 1) // 2
y = (input + x - 1) % (2 ** x)   
if y > x : y = y % x
print("The Manhattan distance between the value",input, "and 0 is", x+y)

memory=[[0 for _ in range(20)] for _ in range(20)]
x,y=10,10

next_directions={(1,0):(0,1) , (0,1):(-1,0) , (-1,0):(0,-1) , (0,-1):(1,0)}
vx, vy = 0,-1
tx,ty=next_directions[(vx,vy)]
value=1
memory[y][x]=value
while value<=input:
    if memory[y+ty][x+tx]==0:
        x,y = x+tx, y+ty
        vx, vy = tx,ty
        tx, ty = next_directions[(tx,ty)]
    else : x,y = x+vx, y+vy
    value=sum(memory[dy][dx] for (dx,dy) in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)])
    memory[y][x]=value
print("The first value written that is larger than", input, "is", value)
