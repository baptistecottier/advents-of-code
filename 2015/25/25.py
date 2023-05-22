from parse import * 

def generator(input):
    return parse("{} row {:d}, column {:d}.", input)[1:3]

def part_1(coordinates):
    row , col = coordinates
    e = (row + col) * (row + col - 1) // 2 - row
    return 20151125 * pow(252533, e, 33554393) % 33554393

def part_2(input):
    return "Merry XMAS"