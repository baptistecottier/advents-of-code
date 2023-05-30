import re

def generator(input): 
    data = []
    for adress in input.splitlines():
        values =  re.split('\[|\]', adress)
        supernet, hypernet = values[::2] , values[1:][::2]
        data.append(('-'.join(supernet), '_'.join(hypernet)))
    return data 

def part_1(adresses): 
    return sum(abba(supernet) and not abba(hypernet) for supernet, hypernet in adresses)

def part_2(adresses): 
    cnt = 0 
    for sn, hn in input: 
        aba = set(sn[i + 1] + sn[i] + sn[i + 1] for i in range(len(sn) - 2) if sn[i] == sn[i + 2] and sn[i] != sn[i + 1])
        cnt += any(item in hn for item in aba)
    return cnt


def abba(s): 
    if any(s[i] != s[i + 1] and \
           s[i] == s[i + 3] and \
           s[i + 1] == s[i + 2] for i in range(len(s) - 3)) : 
        return 1
    return 0