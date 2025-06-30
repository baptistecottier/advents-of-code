"""Advent of Code - Year 2016 - Day 14"""

from re   import search
from pythonfw import functions


def solver(salt: str):
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
    yield get_otp_key(salt, 1)[63]
    yield get_otp_key(salt, 2017)[63]


def get_otp_key(salt: str, recursions: int) -> list[int]:
    """
    Finds the indices of one-time pad (OTP) keys based on MD5 hashes and triplet/quintuplet 
    patterns.

    For each index, generates an MD5 hash (optionally stretched), and checks for quintuplets. If a
    quintuplet is found, searches the previous 1000 hashes for a triplet of the same character. If
    found, adds the index of the triplet to the set of OTP keys. Stops after finding 64 keys and
    processes 1000 more indices to ensure all valid keys are found.

    Args:
        salt (str): The salt string used as a prefix for hashing.
        recursions (int): Number of times to recursively apply the MD5 hash.

    Returns:
        list[int]: Sorted list of indices corresponding to the found OTP keys.
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
                    triplets = search(r'(\w)?\1\1', candidate_hash)
                    if triplets and triplets.group() == target:
                        keys.add(candidate)
        index += 1
    return sorted(set(keys))


def rec_md5(m: str, recursions: int) -> str:
    """Recursively applies MD5 hashing to a string.

    Args:
        m (str): Input string to hash
        recursions (int): Number of times to apply MD5 hash

    Returns:
        str: Final MD5 hash after specified recursions
    """
    for _ in range(recursions):
        m = functions.md5(m)
    return m
