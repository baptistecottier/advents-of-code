import itertools

def generator(input) : 
    trees = []
    grid = [[int(item) for item in list(line)] for line in input.splitlines()]
    
    for (x,y) in itertools.product(range(len(grid)), repeat = 2):
        trees.append([grid[y][x], [grid[y][:x+1][::-1],grid[y][x:],[grid[dy][x] for dy in range(y+1)][::-1] , [grid[dy][x] for dy in range(y,len(grid))]]])
    return trees
    
def part_1(input) : 
    return sum(solver(input, False))
            

def part_2(input) : 
    return max(solver(input, True))


def solver(input, find_best_tree) : 
    out = []
    for [size, views] in input :
        score = 1
        if find_best_tree:
            for view in views :
                cnt = len(list(itertools.takewhile(lambda t : t < size , view[1:])))
                score *= (cnt +( (cnt + 1) != len(view)))
            out.append(score)
        else : out.append(any([max(view) ==  size and view.count(size) <= 1  for view in views]) )
    return out
