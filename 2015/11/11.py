from itertools import *

def generator(input) : 
    return input 

def part_1(input) :
    return solver(input)
    
def part_2(input) : 
    return solver(next_word(solver(input)))

def solver(pw) :
    while(not is_password_ok(pw)) : 
        pw = next_word(pw)
    return pw
    
def is_password_ok(pw):
    return not any(x in pw for x in ['i', 'o', 'l']) and any([ord(b)-ord(a),ord(c)-ord(a)]==[1,2] for ((a,b),c) in zip(zip(pw,pw[1:]), pw[2:])) and sum([len(list(v)) > 1 for _ , v in groupby(pw)]) > 1

def next_word(word):
    l_word , i = list(word) , len(word)-1
    while l_word[i] == 'z':
        l_word[i]='a'
        i-=1
    l_word[i]=chr(ord(l_word[i])+1)
    return "".join(l_word)
        
