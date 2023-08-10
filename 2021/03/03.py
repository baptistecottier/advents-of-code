def preprocessing(input): 
    diagnostic = input.splitlines()
    return (len(diagnostic[0]),  set(int(item, base = 2) for item in diagnostic))

def solver(diagnostic):
    bit_size, report = diagnostic
    
    gamma_rate = sum(2 ** k * most_common_bit(report, k) for k in range(bit_size))
    yield (2 ** bit_size - 1 - gamma_rate) * gamma_rate

    ratings = 1
    for b in {0, 1}:
        diag, k = report, bit_size
        while len(diag) > 1:
            bit  = most_common_bit(diag, k:= k - 1) ^ b
            diag = set(item for item in diag if (item >> k) & 1 == bit)
        ratings *= diag.pop()
    yield ratings

def most_common_bit(report, pos):
    return sum(((r >> pos) & 1) for r in report) >= (len(report) / 2)


    