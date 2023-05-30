import collections

def generator(input):
    return [(room[:-11].replace('-',''), int(room[-10:-7]), room[-6:-1]) for room in input.split()]
    
def part_1(rooms):
    sum_id = 0
    for name, id, checksum in rooms:
        most_common_letters = collections.Counter(sorted(name)).most_common()[:5]
        real_checksum = ''.join(letter for letter, count in most_common_letters)
        if checksum == real_checksum: sum_id += id
    return sum_id    

def part_2(rooms): 
    for name, id, _ in rooms:
        decrypted_name = ''.join(chr(97 + (ord(c) - 97 + id) % 26) for c in name)
        if 'objects' in decrypted_name: return id
