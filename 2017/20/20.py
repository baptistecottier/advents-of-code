from parse import parse

def generator(input): 
    return [parse("p=<{:d},{:d},{:d}>, v=<{:d},{:d},{:d}>, a=<{:d},{:d},{:d}>", line) for line in input.splitlines()]

def part_1(input):
    return min(range(len(input)), key = lambda x:
        (sum([abs(item) for item in input[x][-3:]]), sum([abs(item) for item in input[x][3:6]]), sum([abs(item) for item in input[x][:3]])))

def part_2(input): 
    p = [particule[:3] for particule in input]
    v = [particule[3:6] for particule in input]
    a = [particule[-3:] for particule in input]
    
    for j in range(100):
        p = [[p[i][k] + v[i][k] + (j+1) * a[i][k] for k in range(3)] for i in range(len(p))]
        for i in [i for i in range(len(p) - 1, -1, -1) if p.count(p[i]) != 1]: del p[i], v[i], a[i]
    return len(p)
            
            
        