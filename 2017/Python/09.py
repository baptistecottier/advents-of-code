import re
from AoC_tools import read_input

input=re.sub(r'\!.', '', read_input())


score , step= 0 , 0
garbage=0
garb_count = 0
for char in input:
    if garbage==0 and char== '<' : 
        garbage = 1
    elif garbage == 1 and char== '>' : 
        garbage = 0
    elif garbage==0 :
        if char=='{' : 
            step+=1
            score+=step
        if char=='}' : step-=1
    else:
        garb_count += 1
print(score, garb_count)