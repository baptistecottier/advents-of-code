from ast import parse
import re

with open("Day12/input.txt") as f:
    s=f.read()
    numbers = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s)
    value=0
    for number in numbers:
        value+=sum([int(item) for item in number.split(',')])
    print("Part I : ",value)

from json import loads

def n(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([n(j) for j in j])
    if type(j) != dict:
        return 0
    if 'red' in j.values():
        return 0
    return n(list(j.values()))

print(n(loads(s)))


    # 104046 34786