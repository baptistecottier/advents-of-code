from itertools import product
from parse import parse
from AoC_tools import manhattan_distance
import re

def generator(input): 
    details = []
    for info in input.splitlines()[2:]:
        x, y, size, used, avail, use=parse('/dev/grid/node-x{:d}-y{:d} {:d}T {:d}T {:d}T {:d}%',re.sub(' +', ' ', info))
        details.append([x, y, size, used, avail, use])
    return details

def part_1(input):
    return sum([node_a[3] ** 2 < node_a[3] * node_b[4] for (node_a, node_b) in product(input, input)])

def part_2(input): 
    walls = []
    for node in input : 
        if node[3] == 0 : empty = (node[0], node[1])   
        if node[3] > 100 : walls.append((node[0], node[1]))
    nx, ny = min(walls)
    xx, xy = max(walls)
    if nx == 0 : wall = (xx + 1, xy)
    else : wall = (nx - 1, ny)    
    l = max([n[0] for n in input]) + 1
    return manhattan_distance(empty , wall) + manhattan_distance(wall,(l-1, 0)) + 5*(l-2) # 5 steps are needed for the empty space to contourner the targetted disk
