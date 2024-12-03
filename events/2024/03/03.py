import re

def preprocessing(puzzle_input):
    """
    Take the initial input and remove carriage return as they stop regex expressions
    """
    return puzzle_input.replace("\n", "")

def solver(program):
    """
    For the first part, scan the program for uncorrupted mul operations. 
    Then remove all don't()...do() enclosure and remove the last disabled instructions following a don't()
    """
    yield scan_mul(program)
    program = re.sub(r"don't\(\)(.*?)do\(\)", "", program)
    program = program.split("don't()", 1)[0]
    yield scan_mul(program)
    
def scan_mul(program):
    """
    Use regex expression to extract uncorrupted instructions.
    \d{1,3} allows to extract only numbers with one to three digits.
    Then add the product of matched pairs and return it
    """
    score = 0
    uncorrupted = re.findall(r"mul\((\d{1,3}?),(\d{1,3}?)\)", program)
    for a, b in uncorrupted: 
        score += int(a) * int(b)
    return score

    
