def preprocessing(input: str) -> list[int]:
    return list(int(item) for item in input.splitlines())

def solver(modules: list[int]):
    fuel: int = 0
    modules   = compute_fuel(modules)
    fuel      += sum(modules)
    yield fuel
    while modules:
        modules = compute_fuel(modules)
        fuel    += sum(modules)
    yield fuel


def compute_fuel(modules: list[int]) -> list[int]:
    return [item // 3 - 2 for item in modules if item > 5]