# pylint: skip-file
# flake8: noqa
# type: ignore
"""
Advent of Code - Year 2021 - Day 16
https://adventofcode.com/2021/day/16
"""


def preprocessing(puzzle_input: str) -> str: 
    """
    Converts a hexadecimal string input into its binary representation as a string of bits.
    """
    return "".join(f'{0:04b}'.format(int(n, 16)) for n in puzzle_input)


def solver(transmission):
    yield eval_packet(transmission)
    
    
def eval_packet(packet):
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)
    content = packet[6:]
    match type_id:
        case 0: 
            length_type = int(content[0])
            if length_type == 0:
                sub_packet_length = int(content[1:16], 2)
                sub_packet = content[16:16 + sub_packet_length]

        case 4:
            value = ""
            while True:
                block = content[:5]
                value += block[1:]
                content = content[5:]
                if block[0] == '0': break
            return int(value, 2)