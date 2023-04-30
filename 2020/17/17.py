from itertools import product

def generator(input):
    activated = set()
    size = len(input.splitlines()) // 2
    for y, line in enumerate(input.splitlines()):
        for x, cube in enumerate(line):
            if cube == '#': activated.add((x - size, y - size))
    return activated, size

def part_1(input): return boot_up(({(x, y, 0) for (x, y) in input[0]}, input[1]), 3)

def part_2(input): return boot_up(({(x, y, 0, 0) for (x, y) in input[0]}, input[1]), 4)

def boot_up(input, dimension):
    activated, size = input
    neighbours = [deltas for deltas in product(range(-1, 2), repeat = dimension) if not all(item == 0 for item in deltas)]
    for _ in range(6):
        size += 1
        new_activated = set()
        for coord in product(range(- size, size + 1), repeat = dimension):
            nb = [tuple(t + dt for t, dt in zip(coord, delta)) for delta in neighbours]
            score = sum(n in activated for n in nb)
            if score == 3 or (score == 2 and coord in activated): new_activated.add(coord)
        activated = new_activated
    return len(activated)