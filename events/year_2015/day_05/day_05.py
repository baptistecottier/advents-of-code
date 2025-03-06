"""Advent of Code - Year 2015 - Day 06"""

from itertools import pairwise


def solver(strings: str):
    """Solves the nice string puzzle by checking both old and new rules.

    This function processes a list of strings and counts how many are 'nice' according to
    two different sets of rules:

    Old rules (a string is nice if all conditions are met):
        1. Contains at least three vowels (aeiou)
        2. Contains at least one letter that appears twice in a row
        3. Does not contain the strings: 'ab', 'cd', 'pq', or 'xy'

    New rules (a string is nice if all conditions are met):
        1. Contains a pair of letters that appears at least twice
        2. Contains one letter that repeats with exactly one letter between them

    Args:
        strings (str): A multiline string containing the strings to check

    Yields:
        int: Number of strings that are nice according to the old rules
        int: Number of strings that are nice according to the new rules
    """
    nice_old_rules = 0
    nice_new_rules = 0

    for string in strings.splitlines():

        if any(a == b for a, b in pairwise(string))\
           and sum(string.count(vowel) for vowel in "aeiou") > 2 \
           and not any(pair in string for pair in ('ab','cd','pq','xy')):
            nice_old_rules += 1

        l = len(string) - 1
        if (any(string.count(pair) > 1 for pair in (string[i: i + 2] for i in range(l)))
           and any(a == c and a != b for (a, b, c) in (string[i: i + 3] for i in range(l - 1)))):
            nice_new_rules += 1

    yield nice_old_rules
    yield nice_new_rules
