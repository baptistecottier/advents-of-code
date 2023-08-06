def parser(input): 
    return list(map(int,input))

def solver(captcha):
    def sum_matches(delta):
        return sum(a for (a, b) in zip(captcha, captcha[delta:] + captcha[:delta]) if a == b)
    
    yield sum_matches(1)
    yield sum_matches(len(captcha) // 2)
