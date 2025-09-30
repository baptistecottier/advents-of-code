# pylint: skip-file
# flake8: noqa
# type: ignore

"""
Advent of Code - Year 2021 - Day 19
https://adventofcode.com/2021/day/19
"""


from itertools import permutations, combinations_with_replacement
from pythonfw.functions import extract_chunks

def preprocessing(puzzle_input: str) -> list[list[list[int]]]:
    puzzle_input="""--- scanner 0 ---
-1,-1,1
-2,-2,2
-3,-3,3
-2,-3,1
5,6,-4
8,0,7"""
    scans = []
    scanners_raw = puzzle_input.split('\n\n')

    for scanner_raw in scanners_raw:
        _, beacons_raw = scanner_raw.split('\n', 1)
        beacons = extract_chunks(beacons_raw, 3)
        scans.append((beacons))
        
    return scans


def solver(scans: list[list[list[int]]]) -> tuple[int, int]:
    for scan in scans:
        generate_other_perspectives(scan)
    return (0, 0)


def generate_other_perspectives(scans: list[list[int]]) -> list[list[int]]:
    perspectives = []

    for a, b, c in permutations(range(3), 3):
        for d in combinations_with_replacement((-1, 1), 3):
            perspective = []            
            for s in scans:
                perspective.append([s[a] * d[a], s[b] * d[b], s[c] * d[c]])
            perspectives.append(perspective)
    
    return perspectives

def is_candidate(src: list[int], dst: list[int]):
    return sum(
        sorted(abs(item) for item in s) == sorted(abs(item) for item in d)
        for s, d in zip(src, dst)
        ) >= 12