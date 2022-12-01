import hashlib

sk="bgvyzdsv"
counter=0
hash=""
while hash[:6]!='000000':
    counter+=1
    value_to_hash=sk+str(counter)
    result=hashlib.md5(value_to_hash.encode())
    hash=result.hexdigest()
print(counter)