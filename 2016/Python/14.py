from hashlib import md5
import re

input = 'qzyelonm'

def hash_n_times(s,n): # Doing a loop computing recurisvely n times an hash
    for _ in range(n):
        s=md5(s.encode('utf-8')).hexdigest()
    return s

def find_keys(n) : 
    i,keys=0,[]
    while len(keys) < 70  : # We need to go further te required key amount 
        hash = hash_n_times(input+str(i),n) # We hash n times the value to hash
        for t in range(len(hash)-4) : # Look for 5 successives identical characters
            if all([hash[i]==hash[i+1] for i in range(t, t+4)]): # If there is a match
                target=hash[t] # Stock the repeated character as target
                for j in range(max(0,i-1000)+1,i): # Look in the 1000 previous hashes
                    hash = hash_n_times(input+str(j),n) # Compue the hash
                    triplets=re.findall(r'(\w)?\1\1',hash) # Check all triplets
                    if triplets and triplets[0]==target : # Check that our triplet is the first one !!! 
                        keys.append(j)
                break
        i+=1

    keys=list(set(keys))
    keys.sort()
    return keys[63]

print('Like Pass-Everywhere I got all 64 keys. The index that produced the last key was',  find_keys(1))
print('But apparently MD5 is not secure enough, so let use a 2017-times hashing')
print('That took times but I got the last key, thanks to index',  find_keys(2017))