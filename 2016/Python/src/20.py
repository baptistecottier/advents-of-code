from math import sqrt

goal=29000000


def sum_divisors(n) : 
    total=[]
    for item in range(1,int(sqrt(n))+1):
        if n%item==0  : 
            total.append(item)
            if item**2 != n : total.append(n//item)

    total=[item for item in total if n//item <= 50]
    
    return sum(total)

print([11*sum_divisors(n) for n in range(1,11)])
n=100000
while (11*sum_divisors(n)) < goal :
    if n%10000==0 : print(n,11*sum_divisors(n) ) 
    n+=1
print(n)