def generator(input): return input

def part_1(input): return checksum(input, 272)

def part_2(input): return checksum(input, 35651584)

def checksum(s,disk_length):
    while len(s) < disk_length: s +='0' + ''.join([str(1-(int(b))) for b in s[::-1]])
    s=s[:disk_length] 
    while len(s) % 2 == 0: s = ''.join([str(int(s[i]==s[i+1])) for i in range(0,len(s),2)])
    return s
