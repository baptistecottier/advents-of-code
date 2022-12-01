from dis import Instruction
from AoC_tools import read_input

instructions = [int(item) for item in read_input().splitlines()]
i=instructions[0]
steps=1

while i < len(instructions):
    instructions[i]+=1
    i+=instructions[i]-1
    steps+=1

print(steps)
steps=1
i=instructions[0]

instructions = [int(item) for item in read_input().splitlines()]
while i < len(instructions):
    if instructions[i] != 0 and instructions[i]>2 : 
        instructions[i]-=1
        i+=instructions[i]+1
    else:
        instructions[i]+=1
        i+=instructions[i]-1
    steps+=1

print(steps)