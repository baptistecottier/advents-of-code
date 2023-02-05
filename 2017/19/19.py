def generator(input): 
    return [line for line in input.splitlines()]

def part_1(input):
    return solver(input)[0]
    
def part_2(input): 
    return solver(input)[1]
            
    
def solver(input):
    x, y = input[0].index('|'), 0
    dx, dy = (0, 1)
    letters = []
    steps = 1
    
    while 1:
        done = True
        while input[y+dy][x+dx] != ' ':
            if input[y][x] not in [' ', '|', '-']: letters.append(input[y][x])
            x, y = x + dx, y + dy
            steps += 1

        for nx, ny in [item for item in [(1, 0), (-1, 0), (0, 1), (0, -1)] if item != (- dx, - dy)]:
            if input[y + ny][x + nx] != ' ': 
                dx, dy = nx, ny
                x, y = x + dx, y + dy
                steps += 1
                done = False
                break
            
        if done == True: 
            if input[y][x] not in [' ', '|', '-'] : letters.append(input[y][x])
            return [''.join(letters), steps]
        
