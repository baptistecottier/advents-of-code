def preprocessing(puzzle_input):
    left = []
    right = []
    for pair in puzzle_input.splitlines():
        l, r = pair.split()
        left.append(int(l))
        right.append(int(r))
    return sorted(left), sorted(right)

def solver(left, right):
    distance = 0
    similarity = 0
    for i, l in enumerate(left):
        distance += abs(l - right[i]) 
        similarity += l * right.count(l)
    yield distance
    yield similarity