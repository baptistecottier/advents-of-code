from _md5 import md5
from re   import search

def solver(salt): 
    yield get_OTP_key(salt, 1)[63]
    yield get_OTP_key(salt, 2017)[63]


def get_OTP_key(salt, recursions): 
    hashes = {}
    index, keys = 0, set()
    bound = 50_000
    while index < bound: 
        if index in hashes:
            hash = hashes[index]
        else:
            hash = rec_md5(f"{salt}{index}", recursions)
            hashes[index] = hash
            
        for start in range(28):
            if hash[start: start + 5] == hash[start] * 5:
                target = hash[start: start + 3]
                for candidate in range(max(0, index - 1000) + 1, index):
                    if candidate in hashes:
                        candidate_hash = hashes[candidate]
                    else:
                        candidate_hash = rec_md5(f"{salt}{candidate}", recursions)
                        hashes[candidate] = candidate_hash
                    triplets = search(r'(\w)?\1\1', candidate_hash)
                    if triplets and triplets.group() == target: 
                        keys.add(candidate)
                        if len(keys) == 64: bound = index + 1000
                
        index += 1
    return sorted(set(keys))

def rec_md5(m, recursions): 
    for _ in range(recursions): 
        m = md5(m.encode()).hexdigest()
    return m