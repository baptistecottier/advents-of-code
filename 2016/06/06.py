from collections import Counter

def generator(input):
    return input.splitlines()

def part_1(messages): 
    return correct_code(messages, 0)

def part_2(messages): 
    return correct_code(messages, -1)

def correct_code(messages, order):
    original_message = ""
    for i in range(8):
        letters = (message[i] for message in messages)
        original_message += Counter(letters).most_common()[order][0]
    return original_message