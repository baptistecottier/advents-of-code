def generator(input): 
    inputs = []
    outputs = []
    for digit in input.splitlines():
        i, o = digit.split(' | ', )
        inputs.append([''.join(sorted(ii)) for ii in i.split(' ')])
        outputs.append([''.join(sorted(oo)) for oo in o.split(' ')][::-1])
    return inputs, outputs

def part_1(input): 
    return sum(sum(len(digit) in [2, 4, 3, 7] for digit in output) for output in input[1])

def part_2(input): 
    add_up = 0
    for i, o in zip(*input):
        digits = {}
        for v in i:
            match len(v):
                case 2: digits[1] = v
                case 3: digits[7] = v
                case 4: digits[4] = v                    
                case 7: digits[8] = v
        for v in [item for item in i if item not in digits.values()]:
            match len(v):
                case 5: 
                    if set(digits[1]) < set(v) : digits[3] = v
                    elif set([item for item in digits[4] if item not in digits[1]]) < set(v): digits[5] = v
                    else: digits[2] = v
                case 6:
                    if set(digits[4]) < set(v): digits[9] = v
                    elif set(digits[1]) < set(v): digits[0] = v
                    else: digits[6] = v
        digits = {digits[n]: n for n in digits.keys()}
        add_up += sum(10 ** k * digits[o[k]] for k in range(4))
    return add_up