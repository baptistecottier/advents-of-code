def preprocessing(input_):
    return [int(item) for item in [line.split(' ')[-1] for line in input_.splitlines() if not line.split(' ')[-1].isalpha()]]
          
def solver(input_):
    p = input_[0] - input_[7]
    q = input_[0] - input_[8]
    yield p * q
      
    h = 0
    b = input_[0] * input_[3] - input_[4]
    c = b - input_[5]
    step = - input_[-2]
    for i in range(b, c + 1, step):
        d = input_[7]
        while i % d != 0: d += 1
        if i != d: h += 1
    yield h