def preprocessing(input_): return input_

def part_1(input_): 
    cave = [[0 for _ in range(7)] for _ in range(3000)]
    rocks = [[[1,1,1]], [[0,1,0],[1,1,1],[0,1,0]], [[0,0,1],[0,0,1],[1,1,1]], [[1],[1],[1],[1]], [[1,1],[1,1]]]
