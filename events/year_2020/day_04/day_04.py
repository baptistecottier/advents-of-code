"""
Advent of Code - Year 2020 - Day 4
https://adventofcode.com/2020/day/4
"""

import string


def preprocessing(puzzle_input: str) -> list[dict[str, str]]:
    """
    Parses the puzzle input string into a list of dictionaries, each representing a passport with
    its fields as key-value pairs.
    """
    details = []
    for passport in puzzle_input.split("\n\n"):
        passport = passport.replace("\n", " ")
        infos = {}
        for info in passport.split(" "):
            key, value = info.split(":")
            infos[key] = value
        details.append(infos)
    return details


def solver(passports: list[dict[str, str]]) -> tuple[int, int]:
    """
    Counts the number of candidate and valid passports from a list of passport dictionaries
    according to specific field and validation rules.
    """
    candidates = 0
    valids = 0

    for passport in passports:
        if len(passport) + ("cid" not in passport.keys()) == 8:
            candidates += 1
            if is_valid(passport):
                valids += 1

    return candidates, valids


def is_valid(passport: dict[str, str]) -> bool:
    """
    Checks if a passport dictionary contains valid field values according to specific validation
    rules for each field.
    """
    return all((
        1920 <= int(passport["byr"]) <= 2002,
        2010 <= int(passport["iyr"]) <= 2020,
        2020 <= int(passport["eyr"]) <= 2030,
        any((
            "in" in passport["hgt"] and 59 <= int(passport["hgt"][:-2]) <= 76,
            "cm" in passport["hgt"] and 150 <= int(passport["hgt"][:-2]) <= 193)),
        passport["hcl"].startswith("#") and all(c in string.hexdigits for c in passport["hcl"][1:]),
        passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        len(passport["pid"]) == 9,))
