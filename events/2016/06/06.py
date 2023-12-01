from collections import Counter

def preprocessing(data: str):
    return data.splitlines()

def solver(messages):
    most_commons = ""
    least_commons = ""
    for i in range(len(messages[0])):
        letters = (message[i] for message in messages)
        cntr = Counter(letters).most_common()
        most_commons  += cntr[0][0]
        least_commons += cntr[-1][0]
    yield most_commons
    yield least_commons