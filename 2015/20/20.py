from math import sqrt

def generator(input):
    return int(input)

def part_1(target):
    return find_lucky_house(target // 10, lambda n: 1 + int(sqrt(n)))

def part_2(target):
    return find_lucky_house(target // 11, lambda _: 50)


def find_lucky_house(target, bound):
    def sum_divisors(n):
        return sum(k + (n // k) for k in range(1, 1 + bound(n)) if n % k == 0)
    n = 1
    while sum_divisors(n) < target:
        n += 1
    return n