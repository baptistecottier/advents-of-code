def generator(input):
    boarding_passes = []
    for boarding_pass in input.splitlines():
        boarding_pass = boarding_pass.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
        row = int(boarding_pass[:7], 2)
        column = int(boarding_pass[7:], 2)
        boarding_passes.append(8 * row + column)
    return boarding_passes

def part_1(input):
    return max(input)

def part_2(input):
    for i in range(min(input), max(input)):
        if i not in input: return i
