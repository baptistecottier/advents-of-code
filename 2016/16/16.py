from ast import pattern
from sys import int_info


def generator(input): 
    return list(int(item) for item in input)

def part_1(initial_state): 
    return checksum(initial_state, 272)

def part_2(initial_state): 
    return checksum(initial_state, 35_651_584)

def checksum(state, disk_length):
    while len(state) < disk_length: 
        state += [0] + [1 - b for b in state][::-1]
    state = state[:disk_length]
    while len(state) % 2 == 0: 
        state = [1 - state[i] ^ state[i + 1] for i in range(0, len(state), 2)]
    return ''.join(str(item) for item in state)