from re import findall


def preprocessing(input_):
    return (int(n) for n in findall(r'[0-9]+', input_))


def solver(coordinates):
    row , col = coordinates
    e = (row + col) * (row + col - 1) // 2 - row
    yield 20151125 * pow(252533, e, 33554393) % 33554393