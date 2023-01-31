def generator(input):
    return [[int(i) for i in item.split(': ')] for item in input.splitlines()]

def part_1(input):
    severity=0
    for layer, depth in input : 
        if layer % (2 * (depth - 1)) == 0 : severity += depth * layer
    return severity

def part_2(input):
    delay=1
    while(any([(delay+layer) % (2 * (depth - 1)) == 0  for layer, depth in input])):
        delay += 1
    return delay
