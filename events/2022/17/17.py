def preprocessing(puzzle_input): return puzzle_input

def part_1(puzzle_input): 
    cave = [[0 for _ in range(7)] for _ in range(3000)]
    rocks = [[[1,1,1]], [[0,1,0],[1,1,1],[0,1,0]], [[0,0,1],[0,0,1],[1,1,1]], [[1],[1],[1],[1]], [[1,1],[1,1]]]
