
from pythonfw.functions import md5

def solver(target):
    for trigger in ['00000', '000000']:
        counter = 0
        while not md5(f"{target}{counter}").startswith(trigger):
            counter += 1
        yield counter