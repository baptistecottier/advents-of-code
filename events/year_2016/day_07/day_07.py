"""Advent of Code - Year 2016 - Day 07"""

import re


def preprocessing(puzzle_input: str) -> list[tuple[str, str]]:
    """Process raw puzzle input to extract network addresses.

    This function takes a string input containing network addresses and splits each address
    into supernet and hypernet sequences. Square brackets [] in the input denote hypernet sequences.

    Args:
        puzzle_input (str): Raw input string containing network addresses, one per line

    Returns:
        list: List of tuples where each tuple contains:
            - str: Supernet sequences joined by '-'
            - str: Hypernet sequences joined by '_'

    Example:
        >>> preprocessing("abba[mnop]qrst")
        [('abba-qrst', 'mnop')]
    """
    adresses = []
    for adress in puzzle_input.splitlines():
        values =  re.split(r'\[|\]', adress)
        supernet, hypernet = values[::2] , values[1:][::2]
        adresses.append(('-'.join(supernet), '_'.join(hypernet)))
    return adresses


def solver(adresses: list[tuple[str, str]]):
    """
    Analyzes a list of address tuples to determine support for TLS and SSL protocols.

    Each address is represented as a tuple of two strings: the supernet sequence (sn) and the hypernet
    sequence (hn). The function counts how many addresses support TLS (Transport-Layer Snooping) and
    SSL (Super-Secret Listening) based on the following rules:

    - TLS support: The supernet sequence contains an ABBA pattern and the hypernet sequence does not.
    - SSL support: There exists an ABA pattern in the supernet sequence with a corresponding BAB pattern
        in the hypernet sequence.

    Args:
            adresses (list[tuple[str, str]]): List of tuples, each containing the supernet and hypernet
                    sequences as strings.

    Returns:
            tuple[int, int]: A tuple containing two integers:
                    - The number of addresses that support TLS.
                    - The number of addresses that support SSL.
    """
    cnt_tls_support = 0
    cnt_ssl_support = 0

    for sn, hn in adresses:
        if has_abba(sn) and not has_abba(hn):
            cnt_tls_support += 1
        if has_aba(sn, hn):
            cnt_ssl_support += 1
    return cnt_tls_support, cnt_ssl_support


def has_aba(sn: str, hn: str) -> bool:
    """
    Check if a supernet sequence contains an ABA pattern and its corresponding BAB pattern exists 
    in hypernet.

    An ABA pattern is any three-character sequence which consists of the same characters in first 
    and last positions, and a different character in the middle position.
    A corresponding BAB pattern is the same sequence with the inner and outer characters swapped.

    Args:
        sn (str): Supernet sequence to check for ABA pattern
        hn (str): Hypernet sequence to check for corresponding BAB pattern

    Returns:
        bool: True if a matching ABA-BAB pair is found, False otherwise

    Example:
        >>> has_aba('aba', 'bab')
        True
        >>> has_aba('xyz', 'bab')
        False
    """
    for i in range(len(sn) - 2):
        if sn[i] == sn[i + 2] and sn[i] != sn[i + 1]:
            aba = f"{sn[i + 1]}{sn[i]}{sn[i + 1]}"
            if aba in hn:
                return True
    return False


def has_abba(s: str) -> bool:
    """
    Check if a string contains an ABBA sequence.

    An ABBA sequence is a four-character sequence where:
    - The first and last characters are the same
    - The two middle characters are the same
    - The middle characters are different from the outer characters

    Args:
        s (str): The input string to check

    Returns:
        bool: True if the string contains an ABBA sequence, False otherwise

    Example:
        >>> has_abba("abba")
        True
        >>> has_abba("aaaa")
        False
    """
    for i in range(len(s) - 3):
        if s[i] != s[i + 1] and s[i] == s[i + 3] and s[i + 1] == s[i + 2]:
            return True
    return False
