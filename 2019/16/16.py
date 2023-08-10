def preprocessing(input: int):
    return [int(c) for c in input]

def solver(input):
    yield part_1(input)
    yield part_2(input)
    
def part_1(input: str):
    pattern = [0, 1, 0, -1]
    signal = input
    for _ in range(100):
        signal = [abs(sum(s * pattern[(k + 1) // (i + 1) % 4] for k, s in enumerate(signal))) % 10 for i in range(len(signal))]
    return ''.join(str(n) for n in signal[:8])
    
def part_2(input): 
    offset = int(''.join(str(n) for n in input[:7]))
    signal = input * 10_000
    for _ in range(100):
        partial_sum = 0
        for j in range(len(signal) - 1, offset - 1, -1):
            signal[j] = abs(partial_sum := partial_sum + signal[j]) % 10
    return ''.join(str(n) for n in signal[offset: offset+8])
