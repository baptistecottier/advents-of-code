"""
Advent of Code - Year 2021 - Day 7
https://adventofcode.com/2021/day/7
"""

from statistics import mean, median


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a comma-separated string of numbers into a list of integers.
    """
    return list(map(int, puzzle_input.split(',')))


def solver(crabs) -> tuple[int, int]:
    """
    Calculates the minimum fuel required for crabs to align at the median and mean positions using
    two different cost functions.
    """
    med_crabs = int(median(crabs))
    mean_crabs = int(mean(crabs))
    med_fuel = 0
    mean_fuel = 0

    for crab in crabs:
        med_fuel += abs(crab - med_crabs)
        distance = abs(crab - mean_crabs)
        mean_fuel += distance * (distance + 1) // 2

    return med_fuel, mean_fuel
