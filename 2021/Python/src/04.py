from AoC_tools import read_input
import re 
from time import time

lines=read_input().split('\n\n')
draw=[int(item) for item in lines[0].split(',')]
lines=[list(map(int,re.findall(r'\d+',line.replace('\n',' ')))) for line in lines[1:]]
grids=[[line[c::5] for c in range(5)]+[line[5*c:5*c+5] for c in range(5)] for line in lines]
grids_cpy=grids.copy()

l=5
while len(grids)>0 :
    for grid in grids:
        if any( all(g_item in draw[:l] for g_item in g) for g in grid) : 
            if len(grids)==len(lines) : print('Chosing the first winning board, the final score will be', draw[l-1]*sum([item for item in lines[grids.index(grid)] if item not in draw[:l]]))
            if len(grids)==1 : print('Chosing the last winning board, the final score will be', draw[l-1]*sum([item for item in lines[grids_cpy.index(grids[0])] if item not in draw[:l]]))
            grids.pop(grids.index(grid))
    l+=1

