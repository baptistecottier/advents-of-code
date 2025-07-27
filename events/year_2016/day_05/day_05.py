"""
Advent of Code - Year 2016 - Day 5
https://adventofcode.com/2016/day/5
"""

from pythonfw import functions


def solver(door_id: str) -> tuple[str, str]:
    """
    Solves Day 5 of Advent of Code 2016 password generation puzzle.
    Generates two passwords using MD5 hashing with different methods:
    - Method 1: Uses 6th character of valid hashes sequentially
    - Method 2: Uses 6th character as position, 7th as value

    Args:
        door_id: The door ID string to use as hash prefix

    Returns:
        tuple[str, str]: First 8 characters of method 1 password, complete method 2 password

    Examples:
        >>> solver("abc")
        ("18f47a30", "05ace8e3")
    """
    pw_method_1 = ""
    pw_method_2 = list("________")
    index = 0

    while "_" in pw_method_2:
        md5_hash = functions.md5(f"{door_id}{index}")
        if md5_hash.startswith("00000"):
            pw_index = int(md5_hash[5], 16)
            if pw_index < 8 and pw_method_2[pw_index] == "_":
                pw_method_2[pw_index] = md5_hash[6]
            pw_method_1 += md5_hash[5]
        index += 1

    return pw_method_1[:8], "".join(pw_method_2)
