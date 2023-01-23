import collections

def generator(input):
    return [(room[:-11].replace('-',''), int(room[-10:-7]), room[-6:-1]) for room in input.splitlines()]
    
    
def part_1(input):
    sumid = 0
    for name, id, cs in input:
        count=collections.Counter(name).items()
        count=sorted(count , key = lambda item: (-item[1], item[0]))[:5]
        if all([char in cs for char, _ in count]) : sumid += id
    return sumid


def part_2(input): 
    for name, id, _ in input:
        decrypted_name = ''.join([chr(97 + (ord(c)  - 97 + id) % 26) for c in list(name)])
        if 'northpole' in decrypted_name : return id
