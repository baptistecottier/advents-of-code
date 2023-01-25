from hashlib import md5
import re

def generator(input): return input

def part_1(input): return solver(input, 1)

def part_2(input): return solver(input, 2017)


def solver(input, n) : 
    i,keys=0,[]
    while len(keys) < 70: 
        hash = rec_md5(input + str(i), n)
        for t in range(28) :
            if hash[t:t+5] == hash[t] * 5 :
                target = hash[t]
                for j in range(max(0,i - 1000) + 1, i):
                    hash = rec_md5(input + str(j), n)
                    triplets = re.findall(r'(\w)?\1\1', hash)
                    if triplets and triplets[0] == target: keys.append(j)
                break
        i+=1
    keys=sorted(list(set(keys)))
    return keys[63]

def rec_md5(s,n): 
    for _ in range(n): s = md5(s.encode('utf-8')).hexdigest()
    return s