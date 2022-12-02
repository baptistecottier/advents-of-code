import hashlib

def generator(target) : 
    return target

def part_1(target):
    return solver(target, 5)

def part_2(target):
    return solver(target, 6)

def solver(target, length) :
    counter=0
    hash=""
    while hash[:length]!='0' * length :
        counter+=1
        value_to_hash=target+str(counter)
        result=hashlib.md5(value_to_hash.encode())
        hash=result.hexdigest()
    return counter