from itertools import pairwise

def preprocessing(input): 
    stories = []
    for line in input.splitlines():
        stories.append([int(x) for x in line.split()])
    return stories 


def solver(stories):
    beginning = 0
    ending = 0
    
    for story in stories:
        ending += story[-1]
        beginning += story[0]
        flip = -1
        while not all(n == 0 for n in story):
            story = [b - a for a, b in pairwise(story)]
            ending += story[-1]
            beginning += flip * story[0]
            flip = -flip

    yield ending
    yield beginning

        
