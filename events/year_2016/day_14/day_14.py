"""
Advent of Code - Year 2016 - Day 14
https://adventofcode.com/2016/day/14
"""

from re import search
from pythonfw import functions


def solver(salt: str) -> tuple[int, int]:
    """
    Generates the 64th one-time pad key index for given salt using two different hash stretching
    factors.

    Args:
        salt (str): The input salt string used to generate the one-time pad keys.

    Yields:
        int: The index of the 64th one-time pad key using single hash (stretch factor 1).
        int: The index of the 64th one-time pad key using hash stretching (stretch factor 2017).

    Note:
        The function relies on the external `get_otp_key` function to compute the key indices.
    """
    return get_otp_key(salt)[63], get_otp_key(salt, 2017)[63]


def get_otp_key(salt: str, recursions: int = 1) -> list[int]:
    """
    Generate One-Time Password keys by finding MD5 hashes with specific patterns.

    Args:
        salt: Base string to append indices to for hashing
        recursions: Number of times to recursively hash each value (default: 1)

    Returns:
        Sorted list of indices that form valid OTP keys (up to 64 keys)

    Note:
        A valid key has a triplet pattern and a corresponding quintuplet pattern within the next
        1000 indices.
    """
    hashes = {}
    index, keys = 0, set()
    bound = 50_000
    while index < bound:
        if len(keys) == 64:
            bound = index + 1000
        if index in hashes:
            md5_hash = hashes[index]
        else:
            md5_hash = rec_md5(f"{salt}{index}", recursions)
            hashes[index] = md5_hash

        for start in range(28):
            if md5_hash[start: start + 5] == md5_hash[start] * 5:
                target = md5_hash[start: start + 3]
                for candidate in range(max(0, index - 1000) + 1, index):
                    if candidate in hashes:
                        candidate_hash = hashes[candidate]
                    else:
                        candidate_hash = rec_md5(f"{salt}{candidate}", recursions)
                        hashes[candidate] = candidate_hash
                    triplets = search(r"(\w)?\1\1", candidate_hash)
                    if triplets and triplets.group() == target:
                        keys.add(candidate)
        index += 1
    return sorted(set(keys))


def rec_md5(m: str, recursions: int) -> str:
    """
    Recursively applies MD5 hashing to a string.

    Args:
        m (str): Input string to hash
        recursions (int): Number of times to apply MD5 hash

    Returns:
        str: Final MD5 hash after specified recursions
    """
    for _ in range(recursions):
        m = functions.md5(m)
    return m
