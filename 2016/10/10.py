from collections import defaultdict

def preprocessing(data):
    bots  = defaultdict(list)
    gifts = defaultdict(list)
    
    for instruction in data.splitlines():
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
    

def solver(bots, gifts):
    while (to_distribute := [bot for bot in list(bots.items()) if len(bot[1]) == 2]):
        for bot, microchips in to_distribute:
            microchips.sort()
            if microchips == [17, 61]: 
                yield bot
            low, high = gifts[bot]
            bots[high].append(microchips.pop())
            bots[low].append(microchips.pop())
            
    yield bots[-1].pop() * bots[-2].pop() * bots[-3].pop()

