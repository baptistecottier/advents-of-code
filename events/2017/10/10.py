from pythonfw.y2017 import knot_hash


def solver(input_, n = 256):
    pos     = 0
    size    = n
    numbers = list(range(size))

    try: #Part two includes abritrary ASCII strings, making part I unsolvable 
        for skip, l in enumerate(int(item) for item in input_.split(',')):
            temp = numbers.copy()
            for i in range(l): 
                numbers[(pos + i) % size] = temp[(pos + l - i - 1) % size]
            pos = (pos + l + skip) % size
        yield numbers[0] * numbers[1]
    except:
        yield None

    yield knot_hash(input_, 256)