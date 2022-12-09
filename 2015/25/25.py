from parse import * 

def generator(input):
    [row, col] = parse("To continue, please consult the code grid in the manual.  Enter the code at row {}, column {}.", input)[0:2]
    return [int(row) , int(col)]

def part_1(input) :
    [r , c] = input
    e = (r + c) * (r + c - 1) // 2 - r
    return 20151125 * pow(252533 , e, 33554393) % 33554393

def part_2(input) :
    return input