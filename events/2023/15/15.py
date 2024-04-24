def hash(s):
    h = 0
    for c in s:
        h = 17 * (h + ord(c)) % 256
    return h

def preprocessing(puzzle_input): 
    return puzzle_input.split(',')

def solver(lens):
    sum_hash = 0
    hashes = dict()
    focus_power = 0
    boxes = {n : dict() for n in range(1, 257)}

    for instruction in lens:
        sum_hash += hash(instruction)
        
        if instruction[-1] == '-' :
            label = instruction[:-1]
            if label not in hashes: hashes[label] = hash(label) + 1
            boxes[hashes[label]].pop(label, None)
        else :
            label, focal_length = instruction.split('=')
            if label not in hashes: hashes[label] = hash(label) + 1
            boxes[hashes[label]][label] = int(focal_length)

    for box_id, lenses in boxes.items():
        box_power = 0
        for label, focal_length in enumerate(lenses.values(), 1):
            box_power += label * focal_length
        focus_power += box_power * box_id

    yield sum_hash
    yield focus_power