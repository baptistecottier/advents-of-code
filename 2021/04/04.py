from pythonfw.functions import extract_chunks

def preprocessing(input):
    draw, numbers = input.split('\n\n', 1)
    draw   = [int(number) for number in draw.split(',')]
    boards = extract_chunks(numbers, 25)
    return draw, boards

def solver(draw, boards):
    yield first_win(draw.copy(), boards.copy())
    yield last_lose(draw, boards)
    

def row_and_columns(board): 
    return [set(board[5 * i: 5 * i + 5]) for i in range(5)] + [set(board[i:: 5]) for i in range(5)]

def first_win(draw, boards):
    drew = set(draw[:5]) 
    while True:
        ball = draw.pop(0)
        drew.add(ball)
        for board in boards:
            if any(line < drew for line in row_and_columns(board)): 
                return ball * (sum(n for n in board if n not in drew))

def last_lose(draw, boards):
    while ball:= draw.pop():
        for board in boards: 
            if all(not line < set(draw) for line in row_and_columns(board)):
                return ball * (sum(n for n in board if n not in draw) - ball)