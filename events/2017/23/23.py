def preprocessing(puzzle_input):
    return [int(item) for item in [line.split(' ')[-1] for line in puzzle_input.splitlines() if not line.split(' ')[-1].isalpha()]]
          
def solver(puzzle_input):
    p = puzzle_input[0] - puzzle_input[7]
    q = puzzle_input[0] - puzzle_input[8]
    yield p * q
      
    h = 0
    b = puzzle_input[0] * puzzle_input[3] - puzzle_input[4]
    c = b - puzzle_input[5]
    step = - puzzle_input[-2]
    for i in range(b, c + 1, step):
        d = puzzle_input[7]
        while i % d != 0: d += 1
        if i != d: h += 1
    yield h