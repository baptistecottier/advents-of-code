import _md5
def generator(target): 
    return target

def part_1(target):
    return solver(target, 5)

def part_2(target):
    return solver(target, 6)

def solver(target, length):
    counter = 0
    while (counter := counter + 1) > 0:
        if _md5.md5(f"{target}{counter}".encode()).hexdigest().startswith('0' * length): return counter