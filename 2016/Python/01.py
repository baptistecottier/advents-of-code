# Retrieving the input values as pairs : (turn , distance)
with open("inputs/01.txt") as f: 
    steps=[(step[0],int(step[1:])) for step in f.read().split(', ')]

x , y = 0 , 0 # Starting point
P2 = (0,0) # Answer value for part II
visited_points=[] # Array of visited points
dx , dy = 0 , 1 # Initial direction : North -> (dx,dy) = (0,1)

for turn , dist in steps:
    # After study, the combination that implies a reversal of values are : 
    # (1,0) -> R -> (0,-1)      (-1,0) -> R -> (0,1)      (0,1) -> L -> (-1,0)      (0,-1) -> L -> (1,0)
    # Multiplication by -1 happens when abs(dx)=1 and turn='R' or abs(dx)=0 and turn='L' 
    # This leads to the following condition :
    if abs(dx) == (turn == 'R') : dx , dy = -dx , -dy 
    dx , dy = dy , dx
    
    if not sum(P2) :
        if abs(dy) : # If the direction is vertical, 
            for sy in range(y, y + dy * dist,dy): # For every point we visit
                if [x,sy] in visited_points : P2=(x, sy) # Check if we visit a point we ever visited
                else : visited_points.append([x,sy]) # Otherwise, add this point to the visited points

        if abs(dx) : # If the direction is horizontal, we update the visited points
            for sx in range(x , x + dx * dist , dx): # For every point we visit
                if [sx,y] in visited_points : P2 = (sx,y) # Testing if we visit a point we ever visited
                else : visited_points.append([sx,y]) # Otherwise, add this point to the visited points
    
    x += dx * dist # Update x position
    y += dy * dist # Update y position

print('I started at location (0,0). Easter Bunny HQ is at location ('+str(x)+','+str(y)+'), that is', abs(x)+abs(y), 'blocs away')
print('and the first location I visited twice is at location', P2, 'that is', abs(P2[0])+abs(P2[1]), 'blocs away')