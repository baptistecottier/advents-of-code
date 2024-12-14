from collections import defaultdict

def preprocessing(puzzle_input):
    """From the puzzle input, first group garden plots by their plot name and the 
    associated location, then for each garden plot name, extract regions. Returned
    value is a list of all regions contained in the map of garden plots without 
    their name as they are useless for the rest of the resolution.
    """
    garden_plots = defaultdict(set)
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            garden_plots[c].add((x, y))
    regions = []
    for locations in garden_plots.values():
        regions += extract_regions(locations)
    return regions


def solver(regions):
    """For each region, compute area, length and number of corners of the region.
    As there is as much sides as there is corners those values allow us to compute 
    the initial price and the discount price, respectively answers of part 1 and 
    part 2.
    """
    initial_price = 0
    discount_price = 0
    for region in regions:
        area, length, sides = get_region_morphology(region)
        initial_price += area * length
        discount_price += area * sides   
    yield initial_price
    yield discount_price


def extract_regions(locations):
    """Given a list of locations, this function extracts regions. We start by 
    taking a point in the locations then look for all its neighbours (up, right, 
    down, left). If a neighbour also is in the locations, we add it both to the
    region and the neighbours. For each neighbour met we look for their neighbours 
    and so on while no more neighbours remain, meaning the region is closed.
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
        if region: regions.append(region)
    return regions


def get_region_morphology(region):
    """Given a region, this function returns area, length of the parameter, 
    and the number of corners. To find the perimeter length, for each point, we 
    check if its neighbours are in the region or not. If not, perimeter length is 
    incremented by one for each neighbour found to be not in the region. Then, based
    on the corners patterns below, we can compute the numbers of corners.
    
    Legend: 
        # - location in the region
        . - location not in the region
        ? - location that can be either in or out the region

    (dx, dy) ||     (1, 0)     |     (0, 1)     |     (-1, 0)    |     (0, -1)
    ------------------------------------------------------------------------------
    Group    ||  Outer  Inner  |  Outer  Inner  |  Outer  Inner  |  Outer  Inner  
    ------------------------------------------------------------------------------
             ||   ?.?    ?##   |   ???    ???   |   ???    ???   |   ?.?    .#?
    Pattern  ||   ?#.    ?#.   |   ?#.    ?#.   |   .#?    ##?   |   .#?    ##?
             ||   ???    ???   |   ?.?    ?##   |   ?.?    .#?   |   ???    ???
    """
    corners = 0
    length  = 0
    for (x, y) in sorted(region):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (x + dx, y + dy) not in region: 
                length += 1
                if (x + dy, y - dx) not in region :         # Outer corner
                    corners += 1
                elif (x + dx + dy, y - dx + dy) in region:  # Inner corner
                    corners += 1  
    return len(region), length, corners