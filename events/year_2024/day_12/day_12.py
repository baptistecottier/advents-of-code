"""
Advent of Code - Year 2024 - Day 12
https://adventofcode.com/2024/day/12
"""

from collections import defaultdict


def preprocessing(puzzle_input: str) -> list[list[tuple[int, int]]]:
    """
    Processes the puzzle input to extract and return regions of garden plots grouped by character.
    """
    garden_plots = defaultdict(set)
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            garden_plots[c].add((x, y))
    regions = []
    for locations in garden_plots.values():
        regions += extract_regions(locations)
    return regions


def solver(regions: list[list[tuple[int, int]]]) -> tuple[int, int]:
    """
    Calculates and yields the initial and discount prices for a list of regions based on their
    morphology.
    """
    initial_price = 0
    discount_price = 0
    for region in regions:
        area, length, sides = get_region_morphology(region)
        initial_price += area * length
        discount_price += area * sides
    return initial_price, discount_price


def extract_regions(locations: set[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    """
    Extracts and returns a list of connected regions from a set of (x, y) locations.
    """
    regions = []
    while locations:
        neighbours = [locations.pop()]
        region = set(neighbours)
        while neighbours:
            (x, y) = neighbours.pop()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                candidate = x + dx, y + dy
                if candidate in locations:
                    neighbours.append(candidate)
                    region.add(candidate)
                    locations.remove(candidate)
        if region:
            regions.append(region)
    return regions


def get_region_morphology(region: list[tuple[int, int]]) -> tuple[int, int, int]:
    """
    Given a region, this function returns area, length of the parameter,
    and the number of corners. To find the perimeter length, for each point, we
    check if its neighbours are in the region or not. If not, perimeter length is
    incremented by one for each neighbour found to be not in the region. Then, based
    on the corners patterns below, we can compute the numbers of corners.

    Legend:
        # - location in the region
        . - location not in the region
        ? - location that can be either in or out the region

    (dx, dy) ||     (1, 0)     |     (0, 1)     |    (-1, 0)     |    (0, -1)
    ------------------------------------------------------------------------------
    Group    ||  Outer  Inner  |  Outer  Inner  |  Outer  Inner  |  Outer  Inner
    ------------------------------------------------------------------------------
             ||   ?.?    ?##   |   ???    ???   |   ???    ???   |   ?.?    #.?
    Pattern  ||   ?#.    ?#.   |   ?#.    ?##   |   .#?    .#?   |   .#?    ##?
             ||   ???    ???   |   ?.?    ?.#   |   ?.?    ##?   |   ???    ???
    """
    corners = 0
    length = 0

    for (x, y) in region:
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if (x + dx, y + dy) not in region:
                length += 1
                if (x + dy, y - dx) not in region:         # Outer corner
                    corners += 1
                elif (x + dx + dy, y - dx + dy) in region:  # Inner corner
                    corners += 1
    return len(region), length, corners
