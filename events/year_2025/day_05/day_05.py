"""
Advent of Code - Year 2025 - Day 5
https://adventofcode.com/2025/day/5
"""


def union(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Compute the union of a list of intervals.
    """
    if not intervals:
        return []

    intervals = sorted(intervals)
    merged = [intervals[0]]

    for current_start, current_end in intervals[1:]:
        last_start, last_end = merged[-1]
        if current_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged


def preprocessing(puzzle_input: str) -> tuple[list[int], list[tuple[int, int]]]:
    """
    Extract ranges and IDs from puzzle input.
    """
    _ranges, _ids = puzzle_input.split('\n\n')
    ranges = []
    for _range in _ranges.splitlines():
        _min, _max = tuple(map(int, _range.split('-')))
        ranges.append((_min, _max))
    ranges = union(ranges)  # union returned a sorted list of ranges
    ids = list(map(int, _ids.splitlines()))

    return ids, ranges


def solver(ids: list[int], ranges: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Compute the number of IDs that are fresh, first from the list using a binary search, then all
    available fresh values.
    """
    fresh = 0
    for _id in ids:
        left, right = 0, len(ranges) - 1
        found = False
        while left <= right and not found:
            mid = (left + right) // 2
            if ranges[mid][0] <= _id <= ranges[mid][1]:
                found = True
            elif _id < ranges[mid][0]:
                right = mid - 1
            else:
                left = mid + 1

        if found:
            fresh += 1

    total_fresh_ids = sum(end - start + 1 for (start, end) in ranges)

    return fresh, total_fresh_ids
