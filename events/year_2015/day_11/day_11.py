"""
Advent of Code - Year 2015 - Day 11
https://adventofcode.com/2015/day/11
"""

from itertools import groupby


def solver(password: str) -> tuple[str, str]:
    """
    Solves password-related puzzle by providing two new passwords based on the input.

    Parameters:
        password (str): The initial password to update.

    Returns:
        tuple[str, str]: A tuple containing two updated passwords:
                         - The first password after updating
                         - The second password after updating the next word

    Examples:
        >>> solver("abcdefgh")
        ('abcdffaa', 'abcdffbb')
    """
    password = update_password(password)
    return (update_password(password), update_password(next_word(password)))


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
    Validates a password based on specific rules.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password meets all criteria, False otherwise.

    Rules:
        - Must not contain the letters 'i', 'o', or 'l'
        - Must contain at least two different pairs of repeating letters (e.g., 'aa', 'bb')
        - Must contain at least one increasing straight of three letters (e.g., 'abc', 'bcd')

    Examples:
        >>> is_password_ok("abcdefgh")
        False  # Missing pairs of letters
        >>> is_password_ok("abcdffgg")
        False  # Missing straight
        >>> is_password_ok("abcdeffg")
        True  # Has 'cde' straight and 'ff' pair
        >>> is_password_ok("abcdeffi")
        False  # Contains forbidden letter 'i'
    """
    if any(x in password for x in "iol"):
        return False
    if sum(len(list(v)) > 1 for _, v in groupby(password)) <= 1:
        return False
    for i in range(len(password) - 2):
        if (
            ord(password[i + 1]) - ord(password[i]) == 1
            and ord(password[i + 2]) - ord(password[i]) == 2
        ):
            return True
    return False


def next_word(word: str) -> str:
    """
    Returns the next word by incrementing the last letter, carrying over 'z' to 'a'.

    Args:
        word (str): Input string of lowercase letters.

    Returns:
        str: Next sequential word with incremented letters.

    Examples:
        >>> next_word("abc")
        "abd"
        >>> next_word("abz")
        "aca"
        >>> next_word("azz")
        "baa"
    """
    letters = list(word)
    i = len(word) - 1
    while letters[i] == "z":
        letters[i] = "a"
        i -= 1
    letters[i] = chr(ord(letters[i]) + 1)
    return "".join(letters)
