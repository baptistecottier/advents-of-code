"""Advent of Code - Year 2015 - Day 11"""

from itertools import groupby


def solver(password: str):
    """
    Solves password puzzle by generating two valid passwords.

    Args:
        password (str): Initial password to validate and update

    Yields:
        str: Two consecutive valid passwords that meet security requirements 
    """
    password = update_password(password)
    yield update_password(password)
    yield update_password(next_word(password))


def update_password(password: str) -> str:
    """
    Updates the password to meet the required security criteria.

    This function iterates through possible passwords until finding
    one that meets all security requirements by incrementing the
    current password and checking validity.

    Args:
        password (str): The initial password to be updated

    Returns:
        str: A new password that meets all security requirements

    Example:
        >>> update_password("abcdefgh")
        "abcdffaa"
    """
    while not is_password_ok(password):
        password = next_word(password)
    return password


def is_password_ok(password: str) -> bool:
    """
    Validates a string password based on specific rules:
    - Must not contain 'i', 'o', or 'l'
    - Must contain at least two different pairs of repeating letters
    - Must contain at least one increasing straight of three letters
    """
    if any(x in password for x in "iol"):
        return False
    if sum(len(list(v)) > 1 for _, v in groupby(password)) <= 1:
        return False
    for i in range(len(password) - 2):
        if (ord(password[i + 1]) - ord(password[i]) == 1
            and ord(password[i + 2]) - ord(password[i]) == 2):
            return True
    return False


def next_word(word: str) -> str:
    """Returns the next word by incrementing the last letter, carrying over 'z' to 'a'.

    Args:
        word (str): Input string of lowercase letters.

    Returns:
        str: Next sequential word with incremented letters.
    """
    word = list(word)
    i = len(word) - 1
    while word[i] == 'z':
        word[i] = 'a'
        i -= 1
    word[i] = chr(ord(word[i]) + 1)
    return "".join(word)
