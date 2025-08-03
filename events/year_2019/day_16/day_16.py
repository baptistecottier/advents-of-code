"""
Advent of Code - Year 2019 - Day 16
https://adventofcode.com/2019/day/16
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts the input string of digits into a list of integers.
    """
    return list(map(int, puzzle_input))


def solver(signal: list[int]) -> tuple[str, str]:
    """
    Processes the input signal using two different FFT algorithms and returns their respective
    results as strings.
    """
    return naive_fft(signal), smart_ftt(signal * 10_000)


def naive_fft(signal: list[int]) -> str:
    """
    Applies the Flawed Frequency Transmission (FFT) algorithm to the input signal for 100 phases
    and returns the first eight digits of the final output as a string.
    """
    pattern = [0, 1, 0, -1]

    size = len(signal)
    for _ in range(100):
        new_signal = []
        for i in range(size):
            sig = 0
            for k, s in enumerate(signal):
                index = (k + 1) // (i + 1) % 4
                sig += s * pattern[index]
            new_signal.append(abs(sig) % 10)
        signal = new_signal

    return ''.join(str(n) for n in signal[:8])


def smart_ftt(signal: list[int]) -> str:
    """
    Applies an optimized Fast Fourier Transform (FFT) algorithm to the input signal for 100 phases
    and returns the 8-digit message starting at the offset specified by the first 7 digits of the
    signal.
    """
    offset = int(''.join(str(n) for n in signal[:7]))
    for _ in range(100):
        partial_sum = 0
        for j in range(len(signal) - 1, offset - 1, -1):
            signal[j] = abs(partial_sum := partial_sum + signal[j]) % 10
    return ''.join(str(n) for n in signal[offset: offset+8])
