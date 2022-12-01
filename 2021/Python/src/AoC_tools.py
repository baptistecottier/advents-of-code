import collections
from math import prod 
import os
from sys import argv

def read_input():
    path=argv[0].replace('src', 'inputs').replace('.py', '.txt')
    return open(path, "r").read()

def print_grid(grid, convert=False):
    for g in grid : 
        if isinstance(g, list) : print(''.join(g))
        else : print(g)

def manhattan_distance(x1, x2):
    x1, y1 = x1
    x2, y2 = x2
    return abs(x2-x1)+abs(y2-y1)
    
# BFS algorithm
def bfs(maze, start , end):
    width , height = len(maze[0]) , len(maze)
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x , y) == end:
            return len(path)-1
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and maze[y2][x2] != '#' and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
def chinese_remainder(n, a):
    sum = 0
    p = prod(n)
    for n_i, a_i in zip(n, a):
        p_i = p // n_i
        sum += a_i * mul_inv(p_i, n_i) * p_i
    return sum % p