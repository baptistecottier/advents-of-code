from re import findall

def generator(input):
    all_bags = {}
    input = input.replace("bags","").replace("bag","").replace(".","")
    for rule in input.splitlines():
        color, bags = rule.split("  contain ")[:2]
        if 'no other' in rule: bags = []
        else:
            bags = [b.strip().split(" ",1) for b in bags.split(",")]
            bags = [[int(n), b] for n, b in bags]
        all_bags[color] = bags
    return all_bags

def part_1(input): 
    candidates = ["shiny gold"]
    answer = set()
    while candidates:
        candidate = candidates.pop()
        for color in input.keys():
            if candidate in [c for n,c in input[color]]:
                candidates.append(color)
                answer.add(color)
    return len(answer)

def part_2(input):
    return count_bags("shiny gold", input) - 1
    
def count_bags(color, bags):
    return 1 + sum([n * count_bags(c, bags) for n,c in bags[color]])