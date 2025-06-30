"""Advent of Code - Year 2017 - Day 10"""


def solver(puzzle_input: str, n: int = 256):
    """Compute knot_hash first without then with input/output processing"""
    yield knot_hash(puzzle_input, n, io_processing = False)
    yield knot_hash(puzzle_input, n)


def knot_hash(string: str, size: int, io_processing: bool = True) -> str:
    """
    Compute a knot hash for the given string.
    
    This function implements the knot hash algorithm as described in Advent of Code 2017 Day 10.
    It performs a series of operations on a circular list of numbers based on lengths
    derived from the input string.
    
    Args:
        string: The input string to hash
        size: The size of the numbers list (typically 256)
        io_processing: If True, process input as a string and perform full KnotHash algorithm
                       If False, interpret input as comma-separated integers and return product
                       of first two elements
    
    Returns:
        If io_processing is True, returns a hexadecimal string representing the knot hash
        If io_processing is False, returns the product of the first two elements as a string
    """
    pos = 0
    numbers = list(range(size))
    if io_processing is True:
        lengths = ([ord(k) for k in string] + [17, 31, 73, 47, 23]) * 64
    else:
        lengths = [int(item) for item in string.split(',') if item.strip().isnumeric()]

    for skip, l in enumerate(lengths):
        temp = numbers.copy()
        for i in range(l):
            numbers[(pos + i) % size] = temp[(pos + l - i - 1) % size]
        pos = (pos + l + skip) % size

    if io_processing is True:
        digest = ''
        for k in range(0, 256, 16):
            xor = 0
            for j in numbers[k: 16 + k]:
                xor ^= j
            digest += format(xor, '02x')
    else:
        digest = str(numbers[0] * numbers[1])
    return digest
