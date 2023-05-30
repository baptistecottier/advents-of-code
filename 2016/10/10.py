from collections import defaultdict

def generator(input: str):
    bots  = defaultdict(list)
    gifts = defaultdict(list)
    for instruction in input.splitlines():
        data = instruction.split()
        if data[0] == "value": 
            bots[int(data[-1])].append(int(data[1]))
        else: 
            low  = int(data[6])
            high = int(data[-1])
            if data[5]  == "output": low  = - (low + 1)
            if data[10] == "output": high = - (high + 1)               
            gifts[int(data[1])] = (low, high)
    return bots, gifts

def part_1(instructions): 
    return factory(*instructions, lambda x: x == [17, 61])

def part_2(instructions): 
    return factory(*instructions, lambda x: False)
    
    
def factory(bots, gifts, target):
    while (to_distribute := [bot for bot in list(bots.items()) if len(bot[1]) == 2]):
        for bot, microchips in to_distribute:
            microchips.sort()
            if target(microchips): 
                return bot
            low, high = gifts[bot]
            bots[high].append(microchips.pop())
            bots[low].append(microchips.pop())
    return bots[-1].pop() * bots[-2].pop() * bots[-3].pop()

