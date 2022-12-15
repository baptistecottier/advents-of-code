from parse import parse

def generator(input) : 
    return input

def part_1(input) : 
    no_beacon = set()
    for line in input.splitlines() : 
        [xs, ys, xb, yb]=parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line)[:4]
        md = abs(xb-xs) + abs(yb-ys)
        for dx in range(1 + md - abs(ys - 10)):
            no_beacon.add(xs - dx)
            no_beacon.add(xs + dx)
    return len(no_beacon)-1


def  part_2(input) : 
    no_beacon = [[] for _ in range(4_000_000)]
    for line in input.splitlines() : 
        [xs, ys, xb, yb]=parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line)[:4]
        md = abs(xb-xs) + abs(yb-ys)
        for y in range(max(0,ys-md), min(4_000_000,ys+md)):
            no_beacon[y].append([max(0, xs - (md - abs(ys - y))) , min(4_000_000, xs + (md - abs(ys - y)))])
    for y in range(0, 4_000_000):
        no_beacon[y].sort()
        [mn , mx] = no_beacon[y][0]
        for [a,b] in no_beacon[y] : 
            if a < mn <= b : mn = a
            if a <= mx < b : mx = b
        if mx != 4_000_000 : return (mx + 1) * 4000000 +  y
