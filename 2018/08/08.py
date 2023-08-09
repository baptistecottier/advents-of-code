def preprocessing(input): 
    return [int(item) for item in input.split(' ')]

def solver(tree):
    tree_infos = read_tree(tree)
    yield tree_infos[0]
    yield tree_infos[1]

def read_tree(data):
    children, metas = data[:2]
    data   = data[2:]
    scores = []
    totals = 0

    for _ in range(children):
        total, score, data = read_tree(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0: return (totals, sum(data[:metas]), data[metas:])
    else: return (totals, sum(scores[k - 1] for k in data[:metas] if k <= len(scores)), data[metas:])
