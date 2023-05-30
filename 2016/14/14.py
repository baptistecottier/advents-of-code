from _md5 import md5
import re

def generator(input): 
    return input

def part_1(salt): 
    return get_OTP_key(salt, 1)[63]

def part_2(salt): 
    return get_OTP_key(salt, 2017)[63]


def get_OTP_key(salt, recursions): 
    index, keys = 0, []
    while len(keys) < 70: 
        hash = rec_md5(f"{salt}{index}", recursions)
        for start in range(28):
            if hash[start: start + 5] == hash[start] * 5:
                target = hash[start: start + 3]
                for candidate in range(max(0, index - 1000) + 1, index):
                    candidate_hash = rec_md5(f"{salt}{candidate}", recursions)
                    triplets = re.search(r'(\w)?\1\1', candidate_hash)
                    if triplets and triplets.group() == target: 
                        keys.append(candidate)
        index += 1
    return sorted(list(set(keys)))

def rec_md5(m, recursions): 
    for _ in range(recursions): 
        m = md5(m.encode()).hexdigest()
    return m