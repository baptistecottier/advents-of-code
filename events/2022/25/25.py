def preprocessing(puzzle_input):
    return puzzle_input.splitlines()

def encode(snafu):
    n = 0
    l = len(snafu)
    for index, c in enumerate(snafu, 1):
        match c:
            case '=': c = -2
            case '-': c = -1
            case '0': c = 0
            case '1': c = 1
            case '2': c = 2
        n += c * 5 ** (l - index)
    return n

def decode(decimal):
    numbers = []
    while decimal:
        numbers.append(decimal % 5)
        decimal //= 5
    for index in range(len(numbers)):
        if numbers[index] > 2:
            numbers[index] -= 5
            if index + 1 == len(numbers) : 
                numbers.append(1)
            else : 
                numbers[index + 1] += 1
    return ''.join('=-012'[n + 2] for n in numbers[::-1])
    
def solver(snafus):
    to_supply = sum(encode(snafu) for snafu in snafus)
    yield decode(to_supply)
