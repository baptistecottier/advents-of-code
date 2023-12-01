import collections

def preprocessing(data):
    return [(room[:-11].replace('-',''), int(room[-10:-7]), room[-6:-1]) for room in data.split()]

def solver(rooms):
    sum_id = 0
    for name, id, checksum in rooms:
        if 'objects' in decrypt(name, id): yield (2, id)
        
        common_letters = collections.Counter(sorted(name)).most_common()[:5]
        real_checksum  = ''.join(letter for letter, count in common_letters)
        if checksum == real_checksum: sum_id += id
        
    yield (1, sum_id)

def decrypt(name, id):
    return ''.join(chr(97 + (ord(c) - 97 + id) % 26) for c in name)