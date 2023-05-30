def generator(input):
    return input.splitlines()

def part_1(procedure):
    position = 5 
    code     = ''
    for number in procedure: 
        for instruction in number: 
            match instruction:
                case 'D':
                    if position not in [7, 8, 9]: position += 3
                case 'U': 
                    if position not in [1, 2, 3]: position -= 3
                case 'L':
                    if position not in [1, 4, 7]: position -= 1
                case 'R':
                    if position not in [3, 6, 9]: position += 1
        code += format(position) 
    return code

def part_2(procedure):
    position = 5
    code     = ''
    for number in procedure: 
        for instruction in number: 
            match instruction:
                case 'D': 
                    if   position in [1,11]: position += 2
                    elif position in [2,3,4,6,7,8]: position += 4     
                case 'U': 
                    if   position in [3,13]: position-=2
                    elif position in [6,7,8,10,11,12]: position -= 4
                case 'L':
                    if   position not in [1, 2, 5, 10, 13]: position -= 1
                case 'R':
                    if   position not in [1, 4, 9, 12, 13]: position += 1
        code += format(position,'X')
    return code
