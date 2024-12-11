from collections import defaultdict
from math        import log10


def preprocessing(puzzle_input):
    stones = defaultdict(int)
    for stone in puzzle_input.split():
        stones[int(stone)] += 1
    return blink(stones, 25)


def solver(stones):
    yield sum(stones.values())
    yield sum(blink(stones, 50).values())


def blink(stones, times = 1):
    for _ in range(times):
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
    return new_stones