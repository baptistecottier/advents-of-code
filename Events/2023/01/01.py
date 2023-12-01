
import re
def preprocessing(input):
    document = list()
    for line in input.splitlines():
        matches = re.finditer(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
        numbers = [match.group(1) for match in matches]
        document.append(numbers)
    return document

def solver(document):
    allowed = {str(n): n for n in range(1, 10)}
    yield calibrate(document.copy(), allowed)
    
    allowed.update({
        "one":   1,
        "two":   2,
        "three": 3,
        "four":  4,
        "five":  5, 
        "six":   6,
        "seven": 7,
        "eight": 8, 
        "nine":  9
    })
    yield calibrate(document, allowed)

def calibrate(document, allowed):
    calibration_values = 0
    for digits in document:
        l = 0
        r = len(digits) - 1
        while (a:= digits[l]) not in allowed.keys(): l += 1
        while (b:= digits[r]) not in allowed.keys(): r -= 1
        calibration_values += allowed[a] * 10 + allowed[b]
    return calibration_values
