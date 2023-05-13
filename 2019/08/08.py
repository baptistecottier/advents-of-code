def generator(input):
    return [layer.replace('0', '█').replace('1', ' ') for layer in [input[150 * l: 150 * (l + 1)] for l in range(len(input) // 150)]]

def part_1(input): 
    good_layer = min(input, key = lambda x : x.count('█'))
    return good_layer.count('2') * good_layer.count(' ')

def part_2(input):
    image = ''
    for p in range(len(input[0])):
        i = 0
        while input[i][p] == '2': i += 1
        image += input[i][p]
    return '\n'.join(line for line in (image[25 * i: 25 * (i + 1)] for i in range(6)))