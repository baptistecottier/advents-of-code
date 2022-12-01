input="hepxxzaa"

def is_password_ok(pw):
    if any(x in pw for x in ['i', 'o', 'l']):
        return 0
    elif not (any([ord(pw[i]), ord(pw[i+1]) , ord(pw[i+2])]==[97+j,98+j,99+j] for j in range(24) for i in range(len(pw)-2))):
        return 0
    else :
        for i in range(len(pw)-1):
            for j in range(i+2,len(pw)-1):
                if (pw[i]==pw[i+1] and pw[j]==pw[j+1] and pw[i] != pw[j]):
                    return 1

    return 0

def next_word(word):
    i=len(word)
    l_word=list(word)
    for i in range(len(l_word)-1,-1,-1):
        if l_word[i]=='z':l_word[i]='a'
        else: 
            l_word[i]=chr(ord(l_word[i])+1)
            return "".join(l_word)


pw=input
while(is_password_ok(pw) != 1):
    pw=next_word(pw)

print(pw)
        
