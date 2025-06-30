"""Advent of Code - Year 2016 - Day 05"""

from pythonfw import functions


def solver(door_id: str):
    """
    Generates two password variants for a given door ID using a custom MD5-based algorithm.

    This function computes MD5 hashes of the concatenation of the door ID and an increasing index,
    searching for hashes that start with five zeroes ("00000"). For each such hash:
    - The sixth character is appended to the first password (method 1).
    - If the sixth character is a valid position (0-7) and that position in the second password
        (method 2) is unset, the seventh character is placed at that position.

    The process continues until all positions in the second password are filled.

    Args:
            door_id (str): The door ID used as the base for hash generation.

    Returns:
            tuple[str, str]: A tuple containing:
                    - The first 8 characters found for method 1.
                    - The fully constructed password for method 2.
    """
    pw_method_1 = ''
    pw_method_2 = list('________')
    index = 0

    while '_' in pw_method_2 :
        md5_hash = functions.md5(f"{door_id}{index}")
        if md5_hash.startswith("00000"):
            pw_index = int(md5_hash[5], 16)
            if pw_index < 8 and pw_method_2[pw_index] == '_':
                pw_method_2[pw_index] = md5_hash[6]
            pw_method_1 += md5_hash[5]
        index += 1
    return pw_method_1[:8], ''.join(pw_method_2)
