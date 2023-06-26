import re

def parser(data): 
    adresses = []
    for adress in data.splitlines():
        values =  re.split('\[|\]', adress)
        supernet, hypernet = values[::2] , values[1:][::2]
        adresses.append(('-'.join(supernet), '_'.join(hypernet)))
    return adresses 

def solver(adresses): 
    yield sum(abba(supernet) and not abba(hypernet) for supernet, hypernet in adresses)
    cnt = 0 
    for sn, hn in adresses: 
        aba = set(sn[i + 1] + sn[i] + sn[i + 1] for i in range(len(sn) - 2) if sn[i] == sn[i + 2] and sn[i] != sn[i + 1])
        cnt += any(item in hn for item in aba)
    yield cnt

def abba(s): 
    if any(s[i] != s[i + 1] and \
           s[i] == s[i + 3] and \
           s[i + 1] == s[i + 2] for i in range(len(s) - 3)) : 
        return 1
    return 0