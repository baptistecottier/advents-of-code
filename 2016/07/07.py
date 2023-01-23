import re
def generator(input) : 
    data = []
    for ip in input.splitlines():
        values =  ip.replace('[','-').replace(']','-').split('-')
        ip, hypernet = values[::2] , values[1:][::2]
        data.append((' '.join(ip), ' '.join(hypernet)))
    return data 

def part_1(input) : 
    return sum([abba(ip) and not abba(hn) for ip, hn in input])

def part_2(input) : 
    cnt = 0 
    for ip, hn in input : 
        aba = [ip[i+1]+ip[i]+ip[i+1] for i in range(len(ip)-2) if ip[i] == ip[i+2] and ip[i+1] != ip[i]] 
        cnt += any(item in hn for item in aba)
    return cnt

def abba(s): 
    return any([s[i]==s[i+3] and s[i+1]==s[i+2] and s[i] != s[i+1] for i in range(len(s)-3)])
