def preprocessing(puzzle_input: str):
    boarding_passes: list = []
    for boarding_pass in puzzle_input.splitlines():
        boarding_pass = boarding_pass.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
        row = int(boarding_pass[:7], 2)
        column = int(boarding_pass[7:], 2)
        boarding_passes.append(8 * row + column)
    return sorted(boarding_passes)


def solver(boarding_passes):
    yield boarding_passes[-1]
    seat = boarding_passes[0]
    while seat in boarding_passes: seat += 1
    yield seat