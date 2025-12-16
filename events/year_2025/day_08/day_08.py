"""
Advent of Code - Year 2025 - Day 8
https://adventofcode.com/2025/day/8
"""


def euclidean_distance(pt_a, pt_b):
    """
    Calculate the Euclidean distance between two points in n-dimensional space.
    """
    return sum((a - b) ** 2 for a, b in zip(pt_a, pt_b)) ** 0.5


def preprocessing(puzzle_input: str
                  ) -> tuple[dict[float, tuple[tuple[int, int], tuple[int, int]]], int]:
    """
    Parse input to create distance-coordinate mapping and return point pairs with their euclidean
    distances.
    """
    pts = set()
    coordinates = {}
    for line in puzzle_input.splitlines():
        pt_a = tuple(map(int, line.split(',')))
        for pt_b in pts:
            coordinates[euclidean_distance(pt_a, pt_b)] = (pt_a, pt_b)
        pts.add(pt_a)
    return (coordinates, len(puzzle_input.splitlines()))


def solver(coordinates: dict[float, tuple[tuple[int, int], tuple[int, int]]], l_dist: int
           ) -> tuple[int, int]:
    """
    Solves both parts of the puzzle.
    Returns a tuple (part1_result, part2_result).
    """
    distances = sorted(coordinates)
    circuits: list[set] = []
    checkprod = l_dist

    for n in range(len(coordinates)):

        pt = coordinates[distances[n]]
        print(pt)
        circuits = update_circuits(circuits, pt)

        if l_dist in (len(c) for c in circuits):
            return checkprod, pt[0][0] * pt[1][0]

        if n == 999:
            sorted_lengths = sorted([len(c) for c in circuits])
            checkprod = sorted_lengths[-1] * sorted_lengths[-2] * sorted_lengths[-3]

    raise ValueError("Impossible to connect all pairs")


def update_circuits(circuits, pt):
    """
    Updates circuit connections by merging circuits that share nodes with the given point pair.
    """
    for circuit in circuits[:]:
        for b in [1, 0]:
            if pt[b] in circuit:
                for circuit2 in circuits[:]:
                    if pt[1 - b] in circuit2 and circuit2 != circuit:
                        circuit.update(circuit2)
                        circuits.remove(circuit2)
                circuit.add(pt[1 - b])
                return circuits
    circuits.append(set([pt[0], pt[1]]))
    return circuits
