import itertools
import math 

def generator(input) : 
    grid = [[int(item) for item in list(line)] for line in input.splitlines()]
    return [[grid[y][x], [grid[y][:x+1][::-1],grid[y][x:],[grid[dy][x] for dy in range(y+1)][::-1] , [grid[dy][x] for dy in range(y,len(grid))]]] for x in range(len(grid[0])) for y in range(len(grid)) ]
    
def part_1(input) : 
    return sum([any(max(view) ==  size and view.count(size) <= 1 for view in views) for [size, views] in input])
            

def part_2(input) : 
    return  max([math.prod([len(list(itertools.takewhile(lambda t : t < size , view[1:]))) + (len(list(itertools.takewhile(lambda t : t < size , view[1:]))) != (len(view) -1)) for view in views]) for [size, views] in input])
  
