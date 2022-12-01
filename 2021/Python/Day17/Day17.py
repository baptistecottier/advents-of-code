
def next_step(x,y,vx,vy):
    x , y, vy=x + vx, y+vy, vy-1
    if vx != 0 : vx-=int(vx>0)
    return (x,y,vx,vy)


tx_min, tx_max, ty_min, ty_max = 287, 309, -76, -48
max_y, total = 0, 0

for i in range(tx_max+1):
    for j in range(ty_min, -ty_min):
        vx, vy, x, y, tmax_y= i, j, 0, 0, 0

        while not(x > tx_max or y < ty_min) :
            x,y,vx,vy =next_step(x,y,vx,vy)
            tmax_y=max(tmax_y,y)
            if (tx_min <= x <= tx_max) and (ty_min <= y <= ty_max):
                total+=1
                max_y=max(max_y,tmax_y)
                break
                        
print("Part I : " , max_y, '\nPart II : ', total)