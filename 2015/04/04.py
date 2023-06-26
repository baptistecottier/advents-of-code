import _md5
def parser(target): 
    return target

def solver(target):
    def get_adventcoin(length):
        counter = 0
        while (counter := counter + 1) > 0:
            if _md5.md5(f"{target}{counter}".encode()).hexdigest().startswith('0' * length): 
                return counter
    
    yield get_adventcoin(5)
    yield get_adventcoin(6)