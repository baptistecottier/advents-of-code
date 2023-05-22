import hashlib

def generator(target): 
    return target

def part_1(target):
    return solver(target, 5)

def part_2(target):
    return solver(target, 6)

def solver(target, length):
    counter = 0
    while (counter := counter + 1) > 0:
        if hashlib.md5(f"{target}{counter}".encode()).hexdigest()[:length] == '0' * length: return counter