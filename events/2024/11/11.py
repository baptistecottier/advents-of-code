from collections import defaultdict
from math        import log10

def preprocessing(puzzle_input):
    stones = defaultdict(int)
    for stone in puzzle_input.split():
        stones[int(stone)] += 1
    return stones

def solver(stones):
    for i in range(75):
        if i == 25: yield sum(stones.values())
        new_stones = defaultdict(int)
        for stone, n in stones.items():
            if stone == 0:
                new_stones[1] += n
            elif (log := int(log10(stone))) % 2 == 1:
                new_stones[stone // pow(10, log // 2 + 1)] += n
                new_stones[stone % pow(10, log // 2 + 1)] += n
            else:
                new_stones[2024 * stone] += n
        stones = new_stones
    yield sum(stones.values())