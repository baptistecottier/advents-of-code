from collections import defaultdict

def preprocessing(puzzle_input):
    return list(map(int, puzzle_input.splitlines()))

def solver(secret_numbers):
    sequences = {}
    sum_generated_numbers = 0
    for id, secret_number in enumerate(secret_numbers):
        a, b, c, d = 0, 0, 0, 0
        for rep in range(2_000):
            (a, b, c) = (b, c, d)
            secret_number, d = evolve(secret_number)
            if rep > 2:
                if (id, a, b, c, d) not in sequences:
                    sequences[(id, a, b, c, d)] = secret_number % 10
        sum_generated_numbers += secret_number
    yield sum_generated_numbers
    
    bananas_stock = defaultdict(int)
    for (_, a, b, c, d), bananas in sequences.items():
        bananas_stock[(a, b, c, d)] += bananas
    yield max(bananas_stock.values())
    
def evolve(n):
    temp = mix_and_prune(n << 6, n)
    temp = mix_and_prune(temp >> 5, temp)
    temp = mix_and_prune(temp << 11, temp)
    return temp, (temp % 10) - (n % 10)
  
def mix_and_prune(a, b):
    return (a ^ b) & ((1 << 24) - 1)
    
    