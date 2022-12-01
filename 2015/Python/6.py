def is_nice_string(string):
    if any(x in string for x in ['ab','cd','pq','xy']): return 0
    if any(string[i]==string[i+1] for i in range(len(string)-1)) and (string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u') > 2) : return 1
    return 0

counter=0
with open("Day5/input.txt") as f:
    strings=f.read().splitlines()
    
    for string in strings:
        print(is_nice_string(string))
        counter+=is_nice_string(string)
print(counter)


def is_nice_string_bis(string):
    if any(string[i]==string[i+2] for i in range(len(string)-2)) and any(string.count(string[i]+string[i+1])>1 for i in range(len(string)-1)) : return 1
    return 0

counter=0
with open("Day5/input.txt") as f:
    strings=f.read().splitlines()
    
    for string in strings:
        print(is_nice_string_bis(string))
        counter+=is_nice_string_bis(string)
print(counter)