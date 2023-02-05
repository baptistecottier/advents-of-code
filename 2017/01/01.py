def generator(input): return input 

def part_1(input):
    return solver(input, 1)
    
def part_2(input):    
    return solver(input, len(input) // 2)

def solver(captcha, l):
    return sum([int(captcha[i]) * (captcha[i] == captcha[(i+l) % len(captcha)]) for i in range(len(captcha))])

