from parse import * 

def parser(input):
    return parse("{} row {:d}, column {:d}.", input)[1:3]

def solver(coordinates):
    row , col = coordinates
    e = (row + col) * (row + col - 1) // 2 - row
    yield 20151125 * pow(252533, e, 33554393) % 33554393