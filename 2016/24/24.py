# from AoC_tools import bfs
from itertools import permutations, pairwise
import collections

def generator(input): 
    grid        = input.splitlines()
    coordinates = list(("".join(grid).index(str(i)) % len(grid[0]), "".join(grid).index(str(i)) // len(grid[0])) for i in range(8))
    distances   = [[bfs(grid, src, dst) for dst in coordinates] for src in coordinates]
    return distances

def part_1(distances): 
    paths = set(sum(distances[start][end] for start, end in pairwise([0] + list(path))) for path in permutations(range(8)))
    return min(paths)

def part_2(distances):
    paths = set(sum(distances[start][end] for start, end in pairwise([0] + list(path) + [0])) for path in permutations(range(8)))
    return min(paths)


def bfs(maze, start , end):
    width  = len(maze[0])
    height = len(maze)
    queue  = collections.deque([[start]])
    seen   = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x , y) == end:
            return len(path)-1
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and maze[y2][x2] != '#' and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))