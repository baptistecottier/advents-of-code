from parse import parse
import itertools 

SIZE = 4_000_000
def generator(input) : 
    sensors = []
    for line in input.splitlines() : 
        [xs, ys, xb, yb]=parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line)[:4]
        md = abs(xb-xs) + abs(yb-ys)
        sensors.append([xs, ys, md])
    return sensors

def part_1(input) :
    cnt = set()
    for [xs, ys, md] in input :
            cnt.add(range(xs - (md - abs(ys - SIZE // 2)) , 1 + xs + (md - abs(ys - SIZE // 2))))
    return len(set(list(itertools.chain.from_iterable(cnt)))) - 1

def  part_2(input) : 
    for x , y in itertools.product(range(0,SIZE) , repeat = 2) :
        if all([abs(xs - x) + abs(ys - y) > md for [xs, ys, md] in input]) : return 4_000_000 * x + y 