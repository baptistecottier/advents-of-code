"""Advent of Code - Year 2016 - Day 04"""
from dataclasses import dataclass
import collections

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
    def decrypted_name(self):
        """Returns the decrypted room name by shifting each letter by the sector ID.

        Returns:
            str: The decrypted name using Caesar cipher with sector ID as shift
        """
        return ''.join(chr(97 + (ord(c) - 97 + self.id) % 26) for c in self.name)

    @property
    def real_checksum(self):
        """
        Generates 5-letter checksum from most common letters in name.
        Returns:
            str: Checksum string from 5 most frequent letters
        """
        common_letters = collections.Counter(sorted(self.name)).most_common()[:5]
        return ''.join(letter for letter, _ in common_letters)


def preprocessing(puzzle_input: str) -> list[Room]:
    """Process room data into Room objects.

    Args:
        data (str): Raw room data string with room names, IDs and checksums.

    Returns:
        list[Room]: List of Room objects with parsed name, ID and checksum.
    """
    rooms = []
    for room in puzzle_input.split():
        room_name = room[:-11].replace('-','')
        room_id = int(room[-10:-7])
        room_cs = room[-6:-1]
        rooms.append(Room(room_name, room_id, room_cs))
    return rooms


def solver(rooms: list[Room]):
    """
    Processes a list of Room objects to solve two related puzzles.

    For each room, if the decrypted name contains the substring 'objects', yields a tuple (2, room.id).
    Also, if the room's calculated checksum matches its real checksum, adds the room's id to a running sum.
    At the end, yields a tuple (1, sum_id), where sum_id is the sum of ids of all valid rooms.

    Args:
        rooms (list[Room]): List of Room objects to process.

    Yields:
        tuple[int, int]: (2, room.id) for rooms with 'objects' in their decrypted name.
        tuple[int, int]: (1, sum_id) after processing all rooms, where sum_id is the sum of valid room ids.
    """
    sum_id = 0
    for room in rooms:
        if 'objects' in room.decrypted_name:
            yield (2, room.id)
        if room.cs == room.real_checksum:
            sum_id += room.id
    yield (1, sum_id)
