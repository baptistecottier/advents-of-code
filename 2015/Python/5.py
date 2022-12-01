with open("Day6/input.txt") as f: 
    lights = [[0 for col in range(1000)] for row in range(1000)]
    instructions=f.read().splitlines()
    for instruction in instructions: 
        action, start, _, end=instruction.rsplit(' ',3)
        start_x,start_y = [int(item) for item in start.split(',')]
        end_x,end_y = [int(item) for item in end.split(',')]
        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                if action=='turn on' : lights[x][y]+=1
                if action=='turn off' : lights[x][y]=max(0,lights[x][y]-1)
                if action=='toggle' : lights[x][y]+=2
print(sum(sum(lights,[])))
