from AoC_tools import knot_hash

def generator(input):
    return input

def part_1(input):
    return len(solver(input))

def part_2(instructions):
    regions = 0
    maze = solver(instructions)   
      
    while maze:
        stack = [maze.pop()]
        while stack:
            (x, y) = stack.pop()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                candidate = x + dx, y + dy
                if candidate in maze:
                    stack.append(candidate)
                    maze.remove(candidate)
        regions += 1
    return regions


def solver(instructions):
    maze = set()
    for row in range(128):
        hex_hash = knot_hash(instructions + '-' + str(row),256)
        bin_hash = "{0:128b}".format(int(hex_hash, 16))
        for i, n in enumerate(bin_hash):
            if n == '1':
                maze.add((row, i))
    return maze