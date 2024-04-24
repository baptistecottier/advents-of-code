def preprocessing(puzzle_input: int):
    return [int(c) for c in puzzle_input]


def solver(signal):
    yield naive_fft(signal)
    yield smart_ftt(signal * 10_000)


def naive_fft(signal):
    pattern = [0, 1, 0, -1]
    for _ in range(100):
        signal = [abs(sum(s * pattern[(k + 1) // (i + 1) % 4] for k, s in enumerate(signal))) % 10 for i in range(len(signal))]
    return ''.join(str(n) for n in signal[:8])


def smart_ftt(signal):
    offset = int(''.join(str(n) for n in signal[:7]))
    for _ in range(100):
        partial_sum = 0
        for j in range(len(signal) - 1, offset - 1, -1):
            signal[j] = abs(partial_sum := partial_sum + signal[j]) % 10
    return ''.join(str(n) for n in signal[offset: offset+8])
