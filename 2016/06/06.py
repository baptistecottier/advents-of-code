from collections import Counter
from typing import Iterable

def parser(data: str):
    return data.splitlines()

def solver(messages: list[str]) -> Iterable[str]:
    most_commons:  str = ""
    least_commons: str = ""
    for i in range(len(messages[0])):
        letters = (message[i] for message in messages)
        cntr = Counter(letters).most_common()
        most_commons  += cntr[0][0]
        least_commons += cntr[-1][0]
    yield most_commons
    yield least_commons