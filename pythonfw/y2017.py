def knot_hash(string, size):
    pos     = 0
    numbers = list(range(size))
    lengths = ([ord(k) for k in string] + [17, 31, 73, 47, 23]) * 64
    for skip, l in enumerate(lengths):
        temp = numbers.copy()
        for i in range(l):
            numbers[(pos + i) % size] = temp[(pos + l - i - 1) % size]
        pos = (pos + l + skip) % size
    hash = ''
    for k in range(0, 256, 16):
        xor = 0
        for j in numbers[k: 16 + k]: xor ^= j
        hash += format(xor, '02x')
    return hash