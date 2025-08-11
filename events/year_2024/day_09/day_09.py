"""
Advent of Code - Year 2024 - Day 9
https://adventofcode.com/2024/day/9
"""

from collections import deque
from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts the input string into a list of integers.
    """
    return list(map(int, puzzle_input))


def solver(disk_map: list[int]) -> Iterator[int]:
    """
    Processes a list of disk segment lengths and yields two checksums based on custom memory
    mapping and traversal logic.
    """
    for method in (old_method, new_method):
        yield method(disk_map)


def old_method(disk_map: list[int]) -> int:
    """
    Calculates a checksum from a disk map by simulating disk placement and position-based summation.
    """
    memory = deque([])
    checksum = 0
    position = 0

    for n, length in enumerate(disk_map):
        memory.extend([-1 if n % 2 else n // 2] * length)

    while memory:
        disk_id = memory.popleft()
        while disk_id == -1 and memory:
            disk_id = memory.pop()
        checksum += position * disk_id
        position += 1

    return checksum


def new_method(disk_map: list[int]) -> int:
    """
    Calculates a checksum value based on a custom memory mapping algorithm applied to the input
    disk_map.
    """
    memory = [(-1 if n % 2 else n // 2, length) for n, length in enumerate(disk_map)]
    for i in range(len(memory) - 1, -1, -1):
        (a, n) = memory[i]
        if a != -1:
            for j, (b, m) in enumerate(memory):
                if b == -1:
                    if n < m:
                        memory = memory[:j] + [(a, n), (-1, m - n)] + memory[j + 1:]
                        i -= 1
                        break
                    if n == m:
                        memory = memory[:j] + [(a, n)] + memory[j + 1:]
                        break
    checksum = 0
    disk_id = 0
    seen = set([-1])

    while memory:
        (a, n) = memory.pop(0)
        if a not in seen:
            checksum += a * n * (2 * disk_id + n - 1)
            seen.add(a)
        disk_id += n

    return checksum // 2
