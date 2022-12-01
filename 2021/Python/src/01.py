from AoC_tools import read_input

depths=[int(item) for item in read_input().splitlines()]
size_depths = len(depths)

# Part 1
score = sum([(depths[i+1]>depths[i]) for i in range(size_depths-1)])
print("First score:",score)

# Part 2
score = sum([(depths[i+3]>depths[i]) for i in range(size_depths-3)])
print("Second score:",score)