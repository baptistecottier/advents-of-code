c=0
for x in range(284639,748759):
    b=1
    for i in range(5):
        if str(x)[i]>str(x)[i+1]:
            b=0
            break
    if b!=0:
        for i in range(5):  
            if (str(x)[i]==str(x)[i+1] and ((i==0 and str(x)[i+1]!=str(x)[i+2]) or (i>0 and i<4 and str(x)[i-1]<str(x)[i] and str(x)[i+1]!=str(x)[i+2]) or (i==4 and str(x)[i-1]!=str(x)[i]))):
                c=c+1
                break
print(c)