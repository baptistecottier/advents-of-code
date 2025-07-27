"""
Advent of Code - Year 2016 - Day 4
https://adventofcode.com/2016/day/4
"""

from collections import Counter
from dataclasses import dataclass


@dataclass
class Room:
    """
    A Room represents a room in a security system with encryption.
    Attributes:
        name (str): The encrypted name of the room
        id (int): The sector ID of the room
        cs (str): The given checksum of the room
    Properties:
        decrypted_name: Decrypts the room name using a shift cipher
        real_checksum: Calculates the actual checksum based on letter frequency
    """
    name: str
    id: int
    cs: str

    @property
    def decrypted_name(self) -> str:
        """
        Decrypt the room name by shifting each letter by the room ID.

        Each letter is shifted forward in the alphabet by the room ID amount,
        wrapping around from 'z' to 'a'. Non-alphabetic characters are unchanged.

        Returns:
            str: The decrypted room name.

        Examples:
            >>> room = Room(name="qzmt-zixmtkozy-ivhz", id=343)
            >>> room.decrypted_name()
            'very encrypted name'

            >>> room = Room(name="abc", id=1)
            >>> room.decrypted_name()
            'bcd'
        """
        return "".join(chr(97 + (ord(c) - 97 + self.id) % 26) for c in self.name)

    @property
    def real_checksum(self) -> str:
        """
        Calculate the real checksum of the room name.

        Returns the 5 most common letters in the room name, with ties broken
        alphabetically. Letters are sorted before counting to ensure consistent
        tie-breaking.

        Returns:
            str: A 5-character string representing the checksum.

        Examples:
            >>> room = Room("aaaaa-bbb-z-y-x")
            >>> room.real_checksum()
            'abxyz'

            >>> room = Room("a-b-c-d-e-f-g-h")
            >>> room.real_checksum()
            'abcde'
        """
        common_letters = Counter(sorted(self.name)).most_common()[:5]
        return "".join(letter for letter, _ in common_letters)


def preprocessing(puzzle_input: str) -> list[Room]:
    """
    Parse puzzle input into a list of Room objects.

    Extracts room names (with dashes removed), IDs, and checksums from formatted input strings.
    Each line should contain a room in format: "name-parts-123[abcde]"

    Args:
        puzzle_input (str): Multi-line string with room data

    Returns:
        list[Room]: List of Room objects with parsed name, ID, and checksum

    Examples:
        >>> preprocessing("aaaaa-bbb-z-y-x-123[abxyz]")
        [Room("aaaaabbbbzyx", 123, "abxyz")]

        >>> preprocessing("a-b-c-d-e-f-g-h-987[abcde]\\ntotally-real-room-200[decoy]")
        [Room("abcdefgh", 987, "abcde"), Room("totallyrealroom", 200, "decoy")]
    """
    rooms = []
    for room in puzzle_input.split():
        room_name = room[:-11].replace("-", "")
        room_id = int(room[-10:-7])
        room_cs = room[-6:-1]
        rooms.append(Room(room_name, room_id, room_cs))
    return rooms


def solver(rooms: list[Room]) -> tuple[int, int]:
    """
    Solve room validation and find storage room.

    Args:
        rooms: List of Room objects with id, decrypted_name, cs, and real_checksum attributes.

    Returns:
        tuple[int, int]: Sum of valid room IDs and storage room ID (-1 if not found).

    Examples:
        >>> rooms = [Room(id=123, decrypted_name="storage objects", cs="abc", real_checksum="abc")]
        >>> solver(rooms)
        (123, 123)
    """
    sum_id = 0
    storage_room = -1

    for room in rooms:
        if "objects" in room.decrypted_name:
            storage_room = room.id
        if room.cs == room.real_checksum:
            sum_id += room.id

    return sum_id, storage_room
