def generator(input): return [int(item) for item in input.split(' ')]

def part_1(input): return solver(input)[0]

def part_2(input): return solver(input)[1]


def solver(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for _ in range(children):
        total, score, data = solver(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0: return (totals, sum(data[:metas]), data[metas:])
    else: return (totals, sum(scores[k - 1] for k in data[:metas] if k <= len(scores)), data[metas:])
