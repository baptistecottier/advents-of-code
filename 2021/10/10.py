def generator(input): 
    return input.splitlines()

def part_1(input):
    values = {')': 3, ']':57, '}':1197, '>':25137}
    lines = clean_lines(input, ('','','',''))
    return sum(values[l[0]] for l in lines if l)
        
def part_2(input):
    lines = [int(item[::-1], base = 5) for item in clean_lines(input, ('1','2','3','4')) if set(item) <= {'1','2','3','4'}]
    return sorted(lines)[len(lines) // 2]


def clean_lines(lines, pattern):
    a, b, c, d = pattern
    clean_lines = []
    for line in lines:
        while any(item in line for item in ['()','[]','{}','<>']):
            line = line.replace('()','').replace('[]','').replace('{}','').replace('<>','')
        clean_lines.append(line.replace('(',a).replace('[',b).replace('{',c).replace('<',d))
    return clean_lines