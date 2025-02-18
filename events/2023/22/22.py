from collections import defaultdict
from itertools   import product

def preprocessing(puzzle_input: str) -> list:
    """Process puzzle input to create list of bricks coordinates.

    Takes a string input representing bricks positions with format 'x,y,z~x,y,z' per line,
    where each line defines a brick's start and end coordinates.

    Args:
        puzzle_input (str): Raw input string with brick coordinates.

    Returns:
        list: List of brick coordinate tuples sorted by ascending z coordinate.
              Each brick is represented as ((xa,ya,za), (xb,yb,zb)) where:
              - (xa,ya,za) is the start position
              - (xb,yb,zb) is the end position

    Example:
        >>> preprocessing("1,1,1~1,1,2\\n0,0,1~2,0,1")
        [((0,0,1), (2,0,1)), ((1,1,1), (1,1,2))]
    """
    bricks = list()
    puzzle_input = puzzle_input.replace('~', ',')
    for line in puzzle_input.splitlines():
        xa, ya, za, xb, yb, zb = list(map(int, line.split(',')))
        bricks.append(((xa, ya, za), (xb, yb, zb)))
    return sorted(bricks, key = lambda b : b[0][2])


def solver(bricks):
    """
    Solves the puzzle by analyzing the support structure of bricks and calculating falling
    scenarios.
    Parameters:
    ----------
    bricks : list
        List of bricks with their coordinates and dimensions.
    Yields:
    -------
    int
        First yield: Number of bricks that can be safely disintegrated 
        (those that are not the sole support for any other brick).
    int
        Second yield: Total number of bricks that would fall when each critical
        support brick is disintegrated, excluding the disintegrated bricks themselves.
    Notes:
    -----
    - Uses the `drop_bricks` function (not shown) to calculate support relationships
    - A brick is critical if it's the only support for another brick
    - For each critical brick, calculates cascade of falling bricks
    """
    support = drop_bricks(bricks)
    to_keep = set()
    for _, v in support.items():
        if len(v) == 1:
            to_keep.add(list(v)[0])
    yield len(bricks) - len(to_keep)

    total_falling = 0
    for n in to_keep:
        falling = set([n])
        for k, v in support.items():
            if v.issubset(falling):
                falling.add(k)
        total_falling += len(falling)
    yield total_falling - len(to_keep)


def drop_bricks(bricks) -> set:
    """
    Simulates the falling and stacking of bricks in a 3D space, tracking their support 
    relationships. This function processes a list of bricks defined by their start and end
    coordinates, lets them fall until they reach the ground (z=1) or rest on other bricks, and
    determines which bricks support each other.
    Args:
        bricks: A list of brick coordinates where each brick is defined by two tuples
               ((xa, ya, za), (xb, yb, zb)) representing the start and end points.
    Returns:
        dict: A dictionary with defaultdict(set) where keys are brick indices and
              values are sets of indices of bricks that support the key brick.
    """
    rest = set()
    support = defaultdict(set)
    locations = {}
    for n, ((xa, ya, za), (xb, yb, zb)) in enumerate(bricks):
        cubes = set()
        for x, y, z in product(range(min(xa, xb), max(xa, xb) + 1),
                               range(min(ya, yb), max(ya, yb) + 1),
                               range(min(za, zb), max(za, zb) + 1)):
            cubes.add((x, y, z))

        while (min(z for (_, _, z) in cubes) != 1 and
               not any((x, y, z - 1) in rest for (x, y, z) in cubes)):
            cubes = {(x, y, z - 1) for (x, y, z) in cubes}
        rest.update(cubes)

        for (x, y, z) in cubes:
            locations[(x, y, z)] = n
            if (x, y, z - 1) not in cubes and (x, y, z - 1) in locations:
                support[n].add(locations[(x, y, z - 1)])
    return support
