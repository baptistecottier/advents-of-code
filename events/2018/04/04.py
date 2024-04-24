from parse     import parse
from itertools import pairwise, product

def preprocessing(puzzle_input):
    records = []
    for line in sorted(puzzle_input.splitlines()):
        records.append(parse("[{:d}-{:d}-{:d} {:d}:{:d}]{}", line)[:6])
    return records
    
def solver(records): 
    timesheet = get_timesheet(records)
    lazy_guard = max(timesheet.keys(), key = lambda g: sum(timesheet[g]))
    yield lazy_guard * max(range(60), key = lambda min: timesheet[lazy_guard][min])
    
    lazy_guard, min = max(product(timesheet.keys(), range(60)), key = lambda g: timesheet[g[0]][g[1]])
    yield lazy_guard * min
    
    
def get_timesheet(records):
    timesheet = {}
    for a, b in pairwise(records):
        if 'Guard' in a[-1]:
            guard = get_guard_id(a[-1])
            if guard not in timesheet: timesheet[guard] = [0 for _ in range(60)]
        elif 'Guard' in b[-1]:
            guard = get_guard_id(b[-1])
            if guard not in timesheet: timesheet[guard] = [0 for _ in range(60)]
        elif 'asleep' in a[-1]:
            for i in range(a[-2], b[-2]): timesheet[guard][i] += 1
    return timesheet
        
def get_guard_id(infos):
    return int(infos.split(' ')[2][1:])