"""Advent of Code - Year 2016 - Day 16"""


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Convert a string input into a list of integers.

    Args:
        puzzle_input (str): The input string containing numeric characters.

    Returns:
        list[int]: A list of integers parsed from the input string.

    Example:
        >>> preprocessing("123")
        [1, 2, 3]
    """
    return list(int(item) for item in puzzle_input)


def solver(initial_state: list[int], disk_length: int = 272):
    """
    Generates checksums for a given initial state and disk lengths.

    Args:
        initial_state (list[int]): The initial state of the disk as a list of integers (0s and 1s).
        disk_length (int, optional): The length of the disk to generate the checksum for. Defaults
            to 272.

    Yields:
        int: The checksum for the given initial state and disk length.
        int: The checksum for the given initial state and a disk length of 35,651,584.
    """
    yield checksum(initial_state, disk_length)
    yield checksum(initial_state, 35_651_584)


def checksum(state: list[int], disk_length: int) -> str:
    """
    Generates a checksum for a given initial state and disk length using a modified dragon curve 
    algorithm.

    The function first expands the input state until it reaches the specified disk length by
    appending a 0 and the reversed, bit-flipped version of the current state. It then trims the
    state to the desired disk length. The checksum is computed by repeatedly pairing adjacent bits
    and applying a transformation until the length of the state is odd. The final checksum is 
    returned as a string.

    Args:
        state (list[int]): The initial binary state as a list of 0s and 1s.
        disk_length (int): The desired length of the disk to which the state should be expanded.

    Returns:
        str: The computed checksum as a string of binary digits.
    """
    while len(state) < disk_length:
        state += [0] + [1 - b for b in state][::-1]
    state = state[:disk_length]
    while len(state) % 2 == 0:
        state = [1 - state[i] ^ state[i + 1] for i in range(0, len(state), 2)]
    return ''.join(str(item) for item in state)
