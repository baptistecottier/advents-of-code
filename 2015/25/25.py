from parse import * 

def generator(input):
    return parse("{} row {:d}, column {:d}.", input)[1:3]

def part_1(input) :
    [r , c] = input
    e = (r + c) * (r + c - 1) // 2 - r
    return 20151125 * pow(252533 , e, 33554393) % 33554393

def part_2(input) :
    return "Merry XMAS"