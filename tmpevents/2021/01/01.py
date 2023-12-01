def preprocessing(input):
    return [int(item) for item in input.splitlines()]

def solver(measurements): 
    sum_one   = (measurements[-1] > measurements[-2]) + (measurements[-2] > measurements[-3])
    sum_three = 0
    for i in range(len(measurements) - 3):
        sum_one   += measurements[i + 1] > measurements[i]
        sum_three += measurements[i + 3] > measurements[i]
    yield sum_one
    yield sum_three