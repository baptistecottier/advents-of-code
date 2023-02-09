from parse import parse
import string 

def generator(input):
    instructions = {}
    for step in list(string.ascii_uppercase): instructions[step] = []
    for line in input.splitlines():
        a, b = parse("Step {} must be finished before step {} can begin.", line)
        instructions[b].append(a)
    return instructions

def part_1(input):
    for step in list(string.ascii_uppercase): 
        if input[step] == [] : 
            finished = [step]
            del input[step]
            break
    
    while len(finished) != 26:
        for step in [item for item in list(string.ascii_uppercase) if item not in finished]: 
            if all([item in finished for item in input[step]]): 
                finished.append(step)
                del input[step]
                break
    return ''.join(finished)
        
def part_2(input):
    to_finish, ongoing, finished = [], [], []
    workers = [['',0] for _ in range(5)]
    second = -1
    for step in list(string.ascii_uppercase): 
        if all([item in finished for item in input[step]]): to_finish.append(step)
        
    while len(finished) != 26:
        for w in workers:
            if w[1] == 0 and w[0] != '' : 
                finished.append(w[0])
                available = [item for item in list(string.ascii_uppercase) if item not in finished + to_finish + ongoing]
                for step in available: 
                    if all([item in finished for item in input[step]]): to_finish.append(step)
                        
        for i, w in enumerate(workers):    
            if w[1] == 0:
                w[0] = ''
                if to_finish != [] : 
                    x = to_finish.pop(0)
                    ongoing.append(x)
                    workers[i] = [x, ord(x) - 5]
            w[1] = max(0, w[1]-1)
        second += 1
    return second
       
                

        