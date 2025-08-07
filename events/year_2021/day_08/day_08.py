"""
Advent of Code - Year 2021 - Day 8
https://adventofcode.com/2021/day/8
"""


def preprocessing(puzzle_input: str) -> list[tuple[list[str], list[str]]]:
    """
    Parses the puzzle input into a list of tuples containing sorted signal patterns and output
    values.
    """
    segments = []

    for digit in puzzle_input.replace("|\n", "| ").splitlines():
        signal, value = digit.split(' | ', )
        signal = [''.join(sorted(sig)) for sig in signal.split(' ')]
        value = [''.join(sorted(val)) for val in value.split(' ')][::-1]
        segments.append((signal, value))

    return segments


def solver(segments: list[tuple[list[str], list[str]]]) -> tuple[int, int]:
    """
    Solves the seven-segment display puzzle by counting easily identifiable digits and calculating
    the sum of decoded output values.
    """
    easy = 0
    add_up = 0

    for signal, value in segments:
        digits = {}

        for sig in signal:
            match len(sig):
                case 2: digits[1] = sig
                case 3: digits[7] = sig
                case 4: digits[4] = sig
                case 7: digits[8] = sig

        for sig in (item for item in signal if item not in digits.values()):
            match len(sig):
                case 5:
                    if set(digits[1]) < set(sig):
                        digits[3] = sig
                    elif set(item for item in digits[4] if item not in digits[1]) < set(sig):
                        digits[5] = sig
                    else:
                        digits[2] = sig
                case 6:
                    if set(digits[4]) < set(sig):
                        digits[9] = sig
                    elif set(digits[1]) < set(sig):
                        digits[0] = sig
                    else:
                        digits[6] = sig

        digits = {v: k for k, v in digits.items()}
        for k, sig in enumerate(value):
            d = digits[sig]
            if d in {1, 7, 4, 8}:
                easy += 1
            add_up += 10 ** k * d

    return easy, add_up
