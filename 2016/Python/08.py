from parse import parse
from itertools import product

with open("inputs/08.txt") as f:
    instructions = f.read().splitlines()

width , height = 50 , 6
screen=[[0 for _ in range(width)] for _ in range(height)]


for instruction in instructions : 
    ordre, details=instruction.split(' ', 1) # First part of the message is the instruction
    # rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
    if ordre == 'rect' : 
        w,h=[int(item) for item in details.split('x')] # Extract the dimensions of the rectangle
        for dh , dw in list(product(list(range(h)) , list(range(w)))) : screen[dh][dw]=1 # Generate all the pairs and turn on the corresponding light
    elif ordre == 'rotate' :
        [_,axis,val_axis,shift]=parse("{} {}={:d} by {:d}", details) # Extract rotation parameters

        if axis=='x' : # If rotation is on a vertical axis
            temp_screen=[screen[y][val_axis] for y in range(height)] # Stock the correspond axis value
            for y in range(height): screen[y][val_axis]=temp_screen[(y-shift)%height] # Rotate
        else : # If rotation is on an horizontal axis
            temp_screen=[screen[val_axis][(x-shift)%width] for x in range(width)] # Stock the corresponding axis value
            screen[val_axis]=temp_screen # Rotate
    else : pass

print('It seems there are', sum([sum(g) for g in screen]), 'lit pixels forming the following code :\n','\n|'+'‾'*51+'|')
for g in screen: 
    print('| '+''.join([str(item).replace('0',' ').replace('1', '█') for item in g])+'|')
print('|'+'_'*51+'|')

# leetcode