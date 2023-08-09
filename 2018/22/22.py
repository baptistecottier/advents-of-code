import collections

def preprocessing(input_):
    depth, target = input_.splitlines()
    depth  = int(depth.rsplit(' ')[1])
    tx, ty = tuple(int(n) for n in  (target.split(': ')[1]).split(','))
    line = [0]
    for x in range(1, tx + 50):
        line.append((x * 16807 + depth) % 20183)
    erosion = [line]
    for y in range(1, ty + 50):
        line = [(y * 48271 + depth) % 20183]
        for x in range(1, tx + 50):
            line.append((line[x - 1] * erosion[y - 1][x] + depth) % 20183)
        erosion.append(line)
    erosion = [[item % 3 for item in y] for y in erosion]
    erosion[ty][tx] = 0
    return erosion, tx, ty

def solver(input_):
    yield part_1(input_)
    yield part_2(input_)

def part_1(input_):
    erosion, tx, ty = input_
    return sum(sum(y[:tx + 1]) for y in erosion[:ty + 1])


def part_2(input_): 
    erosion, tx, ty = input_
    path = bfs(erosion, (0, 0), (tx, ty))
    return len(path)


# BFS algorithm
def bfs(maze, start , end):
    width , height = len(maze[0]) , len(maze)
    queue = collections.deque([[(*start, 0, 2)]])
    seen = set(start)
    test = set()
    while queue:
        # print(min(len(p) for p in queue))
        path = queue.popleft()
        x, y, delay, tool = path[-1]
        if delay > 0:
            queue.append(path + [(x, y, delay - 1, tool)])
            continue
        
        else: seen.add((x, y))
        if (x , y) == end:
            if tool == 2:
                if delay == 0:
                    print(path)
                    return len(path)
                else: 
                    queue.append(path + [(x, y, delay - 1, 2)])
            else: 
                queue.append(path + [(x, y, 7,2)])

        else:
            current_type = maze[y][x]
            for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= x2 < width and 0 <= y2 < height and (x2, y2, tool) not in seen:
                    next_type = maze[y2][x2]
                    match current_type, next_type:
                        case 0, 0:
                            queue.append(path + [(x2, y2, 0, tool)])
                        case 1, 1:
                            queue.append(path + [(x2, y2, 0, tool)])
                        case 2, 2:
                            queue.append(path + [(x2, y2, 0, tool)])
                        
                        
                        case 0, 1: 
                            if tool == 1:
                                queue.append(path + [(x2, y2, 0, 1)])
                            elif tool == 2:
                                queue.append(path + [(x2, y2, 6,1)])
                                queue.append(path + [(x2, y2, 6,0)])                            
                            
                                
                        case 0, 2:
                            if tool == 1:
                                queue.append(path + [(x2, y2, 6,2)])
                                queue.append(path + [(x2, y2, 6,0)])
                            elif tool == 2:
                                queue.append(path + [(x2, y2, 0, 2)])
                            

                        case 1, 0: 
                            if tool == 1:
                                queue.append(path + [(x2, y2, 0, 1)])
                            elif tool == 0:
                                queue.append(path + [(x2, y2, 6,1)])
                                queue.append(path + [(x2, y2, 6,2)])                            
                            
                        case 1, 2:
                            if tool == 0:
                                queue.append(path + [(x2, y2, 0, 0)])
                            elif tool == 1:
                                queue.append(path + [(x2, y2, 6,0)])
                                queue.append(path + [(x2, y2, 6,2)])
                            

                        
                        case 2, 0: 
                            if tool == 2:
                                queue.append(path + [(x2, y2, 0, 2)])
                                seen.add((x2, y2, 2))
                            elif tool == 0:
                                queue.append(path + [(x2, y2, 6,2)])                            
                                queue.append(path + [(x2, y2, 6,1)])                            
                            
                        case 2, 1:
                            if tool == 2:
                                queue.append(path + [(x2, y2, 6,0)])                            
                                queue.append(path + [(x2, y2, 6,1)])
                            elif tool == 0:
                                queue.append(path + [(x2, y2, 0, 0)])
                                seen.add((x2, y2, 0))
    return min(test)
