from AoC_tools import read_input, knot_hash

skip=0
size=256
numbers=[i for i in range(size)]
lengths=[int(k) for k in read_input().split(',')]
pos=0
for l in lengths :
    temp=numbers.copy()
    for i in range(l):
        numbers[(pos+i)%size]=temp[(pos+l-i-1) % size]
    pos=(pos+l+skip) % size
    skip+=1
print('Part I:',numbers[0]*numbers[1])

print(knot_hash(read_input(), 256))