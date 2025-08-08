"""
Advent of Code - Year 2023 - Day 15
https://adventofcode.com/2023/day/15
"""


def preprocessing(puzzle_input: str) -> list[str]:
    """
    Splits the input string by commas and returns a list of substrings.
    """
    return puzzle_input.split(',')


def solver(lens: list[str]) -> tuple[int, int]:
    """
    Processes a list of lens instructions to compute the sum of their hashes and the total focus
    power.
    """
    sum_hash = 0
    hashes = {}
    focus_power = 0
    boxes = {n: {} for n in range(1, 257)}

    for instruction in lens:
        sum_hash += hash_algorithm(instruction)

        if instruction[-1] == '-':
            label = instruction[:-1]
            if label not in hashes:
                hashes[label] = hash_algorithm(label) + 1
            boxes[hashes[label]].pop(label, None)

        else:
            label, focal_length = instruction.split('=')
            if label not in hashes:
                hashes[label] = hash_algorithm(label) + 1
            boxes[hashes[label]][label] = int(focal_length)

    for box_id, lenses in boxes.items():
        box_power = 0
        for label, focal_length in enumerate(lenses.values(), 1):
            box_power += label * focal_length
        focus_power += box_power * box_id

    return sum_hash, focus_power


def hash_algorithm(to_hash: str) -> int:
    """
    Computes a custom hash_algorithm value for a given string using a specific iterative algorithm.
    """
    digest = 0
    for char in to_hash:
        digest = 17 * (digest + ord(char)) % 256
    return digest
