from itertools import *

input="1113122113"
out=input
for round in range(50):
    input=out
    out=""
    tmp=','.join(''.join(group) for key, group in groupby(input))
    tmp=tmp.split(',')
    for txt in tmp:
        out+=str(len(txt))+txt[0]
print(len(out))
    