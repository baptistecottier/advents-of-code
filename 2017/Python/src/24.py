with open('inputs/24.txt') as f:
    lines=f.read().splitlines()
grid=[]
for line in lines : grid.append(line)
x=[0 for _ in range(8)]
y=[0 for _ in range(8)]
for g in grid :
    for i in range(8) :  
        try : 
            x[i] , y[i] = grid.index(g) , g.index(str(i))
        except : pass

from collections import deque
from itertools import permutations

neighbours = set([(-1, 0), (1, 0), (0, 1), (0, -1)])
def bfs(grid, src, dest):
	q = deque([(0, src)])
	vis = set([src])
	while q:
		dst, cur = q.pop()
		if cur == dest:
			return dst
		y, x = cur
		for dy, dx in neighbours:
			ny, nx = y + dy, x + dx
			if grid[ny][nx] != '#' and (ny, nx) not in vis:
				q.appendleft((dst+1, (ny, nx)))
				vis.add((ny, nx))


distances_from_0=[bfs(grid, (x[0], y[0]) , (x[i], y[i])) for i in range(8)]
distances=[[bfs(grid, (x[i] , y[i]), (x[j] , y[j]))  for j in range(8) ] for i in range(8) ]
distances
shortest_path1 = shortest_path2=10000
for path in permutations(range(8)):
    path_len=distances_from_0[path[0]]
    path_len += sum([distances[path[i]][path[i+1]] for i in range(len(path)-1)])
    shortest_path1 = min(shortest_path1 , path_len)
    shortest_path2 = min(shortest_path2 , path_len + distances_from_0[path[-1]])
    
print('Part I:' ,shortest_path1)
print('Part II:' ,shortest_path2)

