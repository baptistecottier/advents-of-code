"""
Advent of Code - Year 2023 - Day 5
https://adventofcode.com/2023/day/5
"""

from pythonfw.functions import extract_chunks


def preprocessing(puzzle_input: str) -> tuple[list[int], list[list[list[int]]]]:
    """
    Parses the puzzle input into a list of seed integers and a list of mapping chunks.
    """
    data = puzzle_input.split('\n\n')
    seeds = [int(n) for n in data[0].split(' ')[1:]]
    maps = [extract_chunks(mp, 3) for mp in data[1:]]
    return seeds, maps


def solver(seeds: list[int], maps: list[list[list[int]]]):
    """
    Solves a mapping puzzle by finding the minimum location for given seeds and maps, and yields
    two results based on seed transformations.
    """
    location = set()

    for seed in seeds:
        for mp in maps:
            for (dst, src, size) in mp:
                if seed in range(src, src + size):
                    seed += (dst - src)
                    break
        location.add(seed)

    yield min(location)

    seeds_by_pairs = [seeds[i: i + 2] for i in range(0, len(seeds), 2)]
    maps = maps[::-1]
    loc = 0
    seed = -1

    while (not any(low < seed < low + size for (low, size) in seeds_by_pairs)):
        seed = loc
        for mp in maps:
            for (dst, src, size) in mp:
                if seed in range(dst, dst + size):
                    seed += (src - dst)
                    break
        loc += 1

    yield loc - 1
