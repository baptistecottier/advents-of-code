from AoC_tools import read_input

path=read_input()
further=0
x, y = 0, 0
for step in path.split(','):
    if step == 'ne' :
        x += 1
        y += 1
    elif step == 'se':
        x += 1
    elif step == 's':
        y -= 1
    elif step == 'sw':
        x -= 1
        y -= 1
    elif step == 'nw':
        x -= 1
    elif step == 'n' :
       y += 1
    further=max(further, abs(x)+abs(y))
print(abs(x)+abs(y), further)