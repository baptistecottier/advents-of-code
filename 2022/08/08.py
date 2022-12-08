import itertools

def generator(input) : 
    trees = []
    grid = [[int(item) for item in list(line)] for line in input.splitlines()]
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            trees.append([grid[y][x], [grid[y][:x+1][::-1],grid[y][x:],[grid[dy][x] for dy in range(y+1)][::-1] , [grid[dy][x] for dy in range(y,len(grid))]]])
    return trees
    
def part_1(input) : 
    cnt = 0
    for [size, views] in input :
        for view in views :
            if max(view) ==  size and view.count(size) <= 1 : 
                cnt += 1
                break
    return cnt
            

def part_2(input) : 
    best = 0
    for [size, views] in input :
        score = 1
        for view in views :
            cnt = len(list(itertools.takewhile(lambda t : t < size , view[1:])))
            if cnt != len(view) -1 : cnt += 1
            score *= cnt
        best = max(best, score)
    return best


