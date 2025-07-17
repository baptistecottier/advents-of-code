"""Advent of Code - Year 2015 - Day 06"""

from itertools import pairwise


def solver(strings: str) -> tuple[int, int]:
    """
    Count strings that satisfy nice string criteria according to old and new rules.

    Old rules: has a letter pair, contains at least 3 vowels, no forbidden substrings.
    New rules: has repeating letter pair, contains letter sandwich pattern (aba).

    Examples:
        Old rules:
        - "ugknbfddgicrmopn" is nice (has vowels, double letters, no forbidden substrings)
        - "aaa" is nice (has vowels, double letter, no forbidden substrings)
        - "jchzalrnumimnmhp" is not nice (no double letter)
        - "haegwjzuvuyypxyu" is not nice (contains "xy")

        New rules:
        - "qjhvhtzxzqqjkmpb" is nice (pair "qj" appears twice, has "zxz")
        - "xxyxx" is nice (pair "xx" appears twice, has "xyx")
        - "uurcxstgmygtbstg" is not nice (has repeating pair but no letter sandwich)

    Args:
        strings: Newline-separated strings to evaluate.

    Returns:
        Tuple of (count of nice strings by old rules, count by new rules).
    """
    nice_old_rules = 0
    nice_new_rules = 0

    for string in strings.splitlines():

        if (
            any(a == b for a, b in pairwise(string))
            and sum(string.count(vowel) for vowel in "aeiou") > 2
            and not any(pair in string for pair in ("ab", "cd", "pq", "xy"))
        ):
            nice_old_rules += 1

        l_str = len(string) - 1
        if (
            any(string.count(pair) > 1 for pair in (string[i: i + 2] for i in range(l_str)))
            and any(a == c and a != b for (a, b, c) in (string[i: i + 3] for i in range(l_str - 1)))
        ):
            nice_new_rules += 1

    return nice_old_rules, nice_new_rules
