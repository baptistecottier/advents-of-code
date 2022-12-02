def generator(input) :
    return input.splitlines()

def part_1(strings) :
    return sum([is_nice_string(s) for s in strings])


def part_2(strings) : 
    return sum([is_nicer_string(s) for s in strings])


def is_nice_string(string):
    if any(string[i]==string[i+1] for i in range(len(string)-1)) :
        if (sum([string.count(vowel) for vowel in "aeiou"]) > 2) :
            if not any(x in string for x in ['ab','cd','pq','xy']) :
                return 1
    return 0

def is_nicer_string(string):
    if any(string[i]==string[i+2] and string[i] != string[i+1] for i in range(len(string)-2)) :
        if any(string.count(string[i:i+2])>1 for i in range(len(string)-2)) :
            return 1
    return 0


