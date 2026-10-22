"""
Advent of Code - Year 2021 - Day 16
https://adventofcode.com/2021/day/16
"""


# Standard imports
from collections.abc import Callable, Iterator
from math import inf, prod


OPERATORS: dict[int, Callable[[list[int]], int]] = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1]),
}


def preprocessing(puzzle_input: str) -> str:
    """
    Converts a hexadecimal string input into its binary representation as a string of bits.
    """
    return "".join(f'{int(n, 16):04b}' for n in puzzle_input)


def solver(transmission: str) -> Iterator[int]:
    """
    Decodes the outermost packet. Yields the sum of all version numbers, then the value of the
    expression the packet encodes.
    """
    yield from eval_packet(transmission)[:2]


def eval_packet(packet: str) -> tuple[int, int, str]:
    """
    Decodes the packet at the start of a bit string. Returns the sum of its version numbers
    (subpackets included), its value, and the bits that follow it.
    """
    version_sum = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)
    content = packet[6:]

    if type_id == 4:
        value = ""
        last_group = False
        while not last_group:
            last_group = content[0] == '0'
            value += content[1:5]
            content = content[5:]
        return version_sum, int(value, 2), content

    length_type = content[0]
    if length_type == '0':
        end = 16 + int(content[1:16], 2)
        bits, tail, nb_subpackets = content[16:end], content[end:], inf
    else:
        bits, tail, nb_subpackets = content[12:], "", int(content[1:12], 2)

    # Stops when the subpackets' bits are used up (type 0) or all subpackets are read (type 1)
    sub_packets: list[int] = []
    while bits and len(sub_packets) < nb_subpackets:
        sub_version_sum, sub_value, bits = eval_packet(bits)
        sub_packets.append(sub_value)
        version_sum += sub_version_sum

    return version_sum, OPERATORS[type_id](sub_packets), bits + tail
