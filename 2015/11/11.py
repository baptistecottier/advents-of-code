from itertools import *

def parser(input): 
    return input 

def part_1(pw):
    return update_password(pw)
    
def part_2(pw): 
    pw = update_password(pw)
    return update_password(next_word(pw))


def update_password(pw):
    while (not is_password_ok(pw)): 
        pw = next_word(pw)
    return pw
    
def is_password_ok(pw):
    return  not any(x in pw for x in ['i', 'o', 'l']) and \
            any([ord(pw[i + 1]) - ord(pw[i]), ord(pw[i + 2]) - ord(pw[i])] == [1,2] for i in range(len(pw) - 2)) and \
            sum(len(list(v)) > 1 for _, v in groupby(pw)) > 1

def next_word(word):
    word = list(word)
    i = len(word) - 1
    while word[i] == 'z':
        word[i] = 'a'
        i -= 1
    word[i] = chr(ord(word[i]) + 1)
    return "".join(word)
        
