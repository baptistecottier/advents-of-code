import string 

def generator(input):
    return input

def part_1(input):
    return solver(input, [('','')])

def part_2(input):
    return solver(input, zip(list(string.ascii_lowercase), list(string.ascii_uppercase)))


def solver(input, replace_list):
    new_length = 0 
    shortest_polymer = len(input)
    for a,b in replace_list:
        polymer = input.replace(a, '').replace(b, '')
        length = len(polymer)
        while length != new_length:
            length = len(polymer)
            for a,b in zip(list(string.ascii_lowercase), list(string.ascii_uppercase)):
                polymer = polymer.replace(''.join([a,b]),'').replace(''.join([b,a]),'')
            new_length = len(polymer)
        shortest_polymer = min(shortest_polymer, new_length)
    return shortest_polymer