from AoC_tools import read_input

lines = read_input().splitlines()
patterns , values  = [] , []

for line in lines : 
    p , v = line.split(' | ')
    patterns.append(sorted(p.split(' '), key=len))
    values.append(v.split(' '))

print(sum(sum([len(item) in [2,3,4,7] for item in v]) for v in values))

def is_substring(str1, str2): return all([item in list(set(str2)) for item in list(set(str1))])
output_sum = 0 

for pattern , value in list(zip(patterns, values)) :
    temp = 0 
    for v in value :
        temp *= 10 
        match len(v) :
            case 2 : n=1
            case 3 : n=7
            case 4 : n=4
            case 5 : 
                if is_substring(pattern[1],v) : n=3
                elif sum([item in list(v) for item in list(pattern[2])]) == 2 : n=2
                else : n=5
            case 6 : 
                if is_substring(pattern[2],v) : n=9
                elif is_substring(pattern[1],v) : n=0
                else : n=6
            case 7 : n=8
        temp += n
    output_sum+=temp

print(output_sum)
