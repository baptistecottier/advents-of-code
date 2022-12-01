def print_image(image):
    for line in image : 
        line=''.join(line)
        print(line.replace('0','.').replace('1','#'))
    print('\n')

with open("Day20/input") as f:
    IEA , input_image = f.read().replace('#','1').replace('.','0').split('\n\n')
IEA=IEA.replace('\n','')
input_image=input_image.split('\n')

def upsize_image(image):
    image=['000'+''.join(line)+'000' for line in image]
    output_image=[['0' for x in range(len(image[0]))] for y in range(len(image)+6)]
    for k in range(len(image)):
        output_image[k+3]=image[k]
    return output_image

def set_zeros(image):
    output=[['0' for y in range(len(image[0])+6)] for x in range(len(image)+6)]
    return output

for i in range(2):
    input_image=upsize_image(input_image)
    output_image=set_zeros(input_image)
    
    for x in range(len(input_image)):
        for y in range(len(input_image[0])):
            value=''.join([''.join(input_image[k+1][y:y+3]) for k in [x-1, x, x+1]])
            output_image[x+1][y+1]=IEA[int(value,2)]
    input_image=output_image.copy()
    print_image(input_image)
total=0
for line in input_image[3:-16]:
    total+=sum(list(map(int,line[3:-16])))
print(total)


# Part 1: 4964
# Part 2: 13202
