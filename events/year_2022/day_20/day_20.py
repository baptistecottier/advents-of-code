"""
Advent of Code - Year 2022 - Day 20
https://adventofcode.com/2022/day/20
"""

from collections.abc import Iterator


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts the puzzle input string into a list of integers, one per line.
    """
    return list(map(int, puzzle_input.splitlines()))


def solver(file: list[int]) -> Iterator[int]:
    """
    Yields the result of mixing the input list with different parameters for number of mixes and
    decryption status.
    """
    for n_mix, decrypted in ((1, False), (10, True)):
        yield mix(file, n_mix, decrypted)


def mix(file: list[int], n_mix: int, decrypted=False):
    """
    Mixes a list of integers according to a custom shuffling algorithm and returns the sum of
    values at specific offsets from the zero value.
    """
    if decrypted:
        file = [811589153 * i for i in file]

    nb_cipher = len(file)
    index_list = list(range(nb_cipher))

    for _ in range(n_mix):
        for index, cipher in enumerate(file):
            prev_index = index_list.index(index)
            index_list.remove(index)
            index_list.insert((cipher + prev_index) % (nb_cipher - 1), index)

    zero_index = index_list.index(file.index(0))
    return sum(file[index_list[(zero_index + shift) % nb_cipher]] for shift in [1000, 2000, 3000])
