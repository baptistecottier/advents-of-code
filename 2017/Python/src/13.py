from AoC_tools import read_input, chinese_remainder


input = [[int(i) for i in item.split(': ')] for item in read_input().splitlines()]
print(input)

severity=0
for layer, depth in input : 
    if layer % (2 * (depth - 1)) == 0 : severity += depth * layer
print(severity)

delay=1
while(any([(delay+layer) % (2 * (depth - 1)) == 0  for layer, depth in input])):
    delay += 1

print(delay)



