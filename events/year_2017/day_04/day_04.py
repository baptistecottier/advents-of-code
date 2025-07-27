"""
Advent of Code - Year 2017 - Day 4
https://adventofcode.com/2017/day/4
"""


def preprocessing(puzzle_input: str) -> list[list[str]]:
    """
    Converts the puzzle input into a list of words

    Example:
      >>> preprocessing("aa bb"\n"cc dd aaa")
      [["aa", "bb"], ["cc", "dd", "aaa"]]
    """
    return [passphrase.split(" ") for passphrase in puzzle_input.splitlines()]


def solver(passphrases: list[list[str]]) -> tuple[int, int]:
    """
    Validate passphrases according to two security criteria.

    Args:
        passphrases: List of passphrases, each being a list of words.

    Yields:
        int: Number of passphrases with no duplicate words.
        int: Number of passphrases with no words that are anagrams of each other.
    """
    valid = 0
    safer_valid = 0

    for passphrase in passphrases:
        if len(passphrase) == len(set(passphrase)):
            valid += 1
            if len(set("".join(sorted(p)) for p in passphrase)) == len(passphrase):
                safer_valid += 1

    return valid, safer_valid
