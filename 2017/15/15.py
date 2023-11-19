def preprocessing(input):
    items = input.split()
    return int(items[4]), int(items[9])

def solver(genA, genB): 
    first_logic_count = 0
    second_logic_genA = []
    second_logic_genB = []
    
    for _ in range(40_000_000):
        genA = (genA * 16807) % 2147483647
        genB = (genB * 48271) % 2147483647

        if (genA - genB) % (2 ** 16) == 0: first_logic_count += 1
        if genA % 4 == 0: second_logic_genA.append(genA)
        if genB % 8 == 0: second_logic_genB.append(genB)

    yield first_logic_count
    yield sum((genA - genB) % (2 ** 16) == 0 for genA, genB in zip(second_logic_genA, second_logic_genB))
