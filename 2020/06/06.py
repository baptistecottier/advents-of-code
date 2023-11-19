from collections import Counter
from typing      import Generator 


def preprocessing(input: str) -> Generator[list[str], None, None]:
    return (group.splitlines() for group in input.split('\n\n'))


def solver(groups: Generator[list[str], None, None]) -> Generator[int, None, None]:
    anyone: int   = 0
    everyone: int = 0
    
    for group in groups:
        answers   = tuple(c for _, c in Counter(''.join(group)).most_common() if c >= 1)
        anyone   += len(answers)
        everyone += len(tuple(answer for answer in answers if answer == len(group)))
        
    yield anyone        
    yield everyone