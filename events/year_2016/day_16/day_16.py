"""
Advent of Code - Year 2016 - Day 16
https://adventofcode.com/2016/day/16
"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Convert a string of digits to a list of integers.

    Args:
        puzzle_input (str): String containing digits to convert.

    Returns:
        list[int]: List of integers parsed from the input string.
    """
    return list(int(item) for item in puzzle_input)


def solver(initial_state: list[int], disk_length: int = 272) -> tuple[str, str]:
    """
    Solve the disk filling puzzle by generating checksums for two different disk lengths.

    Args:
        initial_state: List of integers representing the initial dragon curve state
        disk_length: Length of the first disk to fill (default: 272)

    Returns:
        Tuple containing checksums for the specified disk length and 35,651,584
    """
    return checksum(initial_state, disk_length), checksum(initial_state, 35_651_584)


def checksum(state: list[int], disk_length: int) -> str:
    """
    Generate a checksum for a disk of specified length using dragon curve expansion.

    Expands the initial state using the dragon curve algorithm (append 0 followed by
    the bitwise complement of the reverse) until reaching the target disk length,
    then computes a checksum by iteratively XORing adjacent pairs until the result
    has odd length.

    Args:
        state: Initial binary state as list of integers (0 or 1)
        disk_length: Target length for the disk

    Returns:
        Final checksum as a string of binary digits
    """
    while len(state) < disk_length:
        state += [0] + [1 - b for b in state][::-1]
    state = state[:disk_length]
    while len(state) % 2 == 0:
        state = [1 - state[i] ^ state[i + 1] for i in range(0, len(state), 2)]
    return "".join(str(item) for item in state)
