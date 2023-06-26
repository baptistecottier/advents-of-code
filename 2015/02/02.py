def parser(data):
    boxes = list(sorted(tuple(int(size) for size in present.split('x'))) for present in data.splitlines())
    return boxes

def solver(dimensions: list[tuple[int]]) -> int:
    yield sum(2 * h * (l + w) + 3 * l * w for l, w, h in dimensions)
    yield sum(2 * (l + w) + l * w * h for l, w, h in dimensions)
