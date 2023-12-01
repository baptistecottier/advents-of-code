def preprocessing(input):
    return input.splitlines()

def solver(rucksacks):
    priorites = {c: ord(c) - 96 for c in 'abcdefghijklmonpqrstuvwxyz'}
    priorites.update({c: ord(c) - 38 for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'})
    items_priority  = 0
    badges_priority = 0

    for ga, gb, gc in (rucksacks[n: n + 3] for n in range(0, len(rucksacks), 3)):
        for sack in (ga, gb, gc):
            item = set(sack[:len(sack) // 2]).intersection(set(sack[len(sack) // 2:])).pop()
            items_priority += priorites[item]
        badge = set(ga).intersection(set(gb)).intersection(set(gc)).pop()
        badges_priority += priorites[badge]

    yield items_priority
    yield badges_priority