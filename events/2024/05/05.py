def preprocessing(puzzle_input):
    """
    Puzzle input contains two parts.
    The first one contains ordering rules and the second one a list of updates.
    We associate each update with an initial value of 0 supposing the update does 
    not need to be ordered, for further purpose.
    """
    raw_rules, raw_updates = puzzle_input.split('\n\n')
    rules, updates = [], []
    
    for rule in raw_rules.splitlines():
        rules.append([int(page) for page in rule.split('|')])
        
    for update in raw_updates.splitlines():
        updates.append((0, [int(page) for page in update.split(',')]))
    return rules, updates


def solver(rules, updates):
    """
    To solve both parts, we take updates one after the other. For each update, we check if all 
    pairs match a rule. 
    
    If not, we swap that pair and append the new update to the list of updates with the to_order 
    value set to 1.
    
    If so, its middle page is added to the correct sum depending on the value of to_order
    
    Answer of part 1 is given by the first value of the middle_page_sum vector, while answer of 
    part 2 is given by the second value.
    """
    middle_page_sum = [0, 0]
    while updates:
        to_order, update = updates.pop()
        ordered = True
        for i in range(len(update) - 1):
            if [update[i], update[i + 1]] not in rules:
                update[i], update[i + 1] = update[i + 1], update[i]
                updates.append((1, update))
                ordered = False
                break
        if ordered:
            middle_page_sum[to_order] += update[len(update) // 2]
            
    for n in middle_page_sum: yield n