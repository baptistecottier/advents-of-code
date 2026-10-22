"""
Advent of Code - Year 2019 - Day 25
https://adventofcode.com/2019/day/25
"""

# Standard imports
import re
from collections.abc import Iterator
from copy import deepcopy
from itertools import combinations

# First party imports
from events.year_2019.ship_computer import Program


def preprocessing(puzzle_input: str) -> list[int]:
    """
    Converts a comma-separated string of integers into a list of integers.
    """
    return list(map(int, puzzle_input.split(',')))


def solver(intcode: list[int]) -> Iterator[int]:
    """
    Explores the ship with the droid, picking up every safe item, then tries combinations of items
    at the security checkpoint until the pressure-sensitive floor lets the droid through. Yields the
    airlock password.
    """
    droid = Program(intcode)
    items: list[str] = []
    path = explore(droid, send(droid), None, items)
    if path is None:
        raise ValueError("No pressure-sensitive floor found")

    # Go to the pressure-sensitive floor
    for door in path[:-1]:
        send(droid, door)

    # Find the perfect items combination that simulate the correct weight
    for size in range(len(items) + 1):
        for kept in combinations(items, size):
            trial = deepcopy(droid)
            for item in items:
                if item not in kept:
                    send(trial, f"drop {item}")
            if password := re.search(r"typing (\d+)", send(trial, path[-1])):
                yield int(password.group(1))
                return
    raise ValueError("No combination of items gets through the checkpoint")


def explore(droid: Program, room: str, back: str | None, items: list[str]) -> list[str] | None:
    """
    Visits every room reachable from the current one with a depth-first search, taking every safe
    item on the way, then comes back. Returns the doors leading from the current room to the
    pressure-sensitive floor, or None if it is not reachable this way.
    """
    traps = {"escape pod", "giant electromagnet", "infinite loop", "molten lava", "photons"}
    opposite = {"north": "south", "south": "north", "east": "west", "west": "east"}
    path: list[str] | None = None
    doors: list[str] = []
    for item in re.findall(r"^- (.+)$", room, re.M):
        if item in traps:
            continue
        if item not in opposite:
            send(droid, f"take {item}")
            items.append(item)
        else:
            doors.append(item)

    for door in doors:
        if door == back:
            continue
        text = send(droid, door)
        if text.count("==") > 2:
            # Ejected from the pressure-sensitive floor back to the checkpoint
            path = [door]
            continue
        if (sub_path := explore(droid, text, opposite[door], items)) is not None:
            path = [door, *sub_path]
        send(droid, opposite[door])
    return path


def send(droid: Program, command: str = "") -> str:
    """
    Types a command to the droid, if any, and returns its answer up to the next prompt.
    """
    signal = list(f"{command}\n".encode()) if command else []
    text = ""
    output = droid.run(*signal)
    while output is not None:
        text += chr(output)
        output = droid.run()
    return text
