import re

with open("inputs/03.txt") as f:
    triangles=f.read().splitlines()

count=0
for triangle in triangles : 
    sides = ([int(item) for item in re.findall('[0-9]+', triangle)]) # Extract side length
    sides.sort() # Sort in ascending order
    if sides[0]+sides[1]>sides[2] : count += 1 # If the sum of the two smallest sides is lower than the greatest side, increas the count

print('There is', count, 'possibles triangles')


count , i = 0 ,0
triangles=list(zip(triangles[:3]))
print(triangles)
# while i+6 < len(lengths):
#     sides=sorted([lengths[i], lengths[i+3] , lengths[i+6]]) # Retrieve the group and sort them
#     if sides[0]+sides[1]>sides[2] : count += 1 # If the sum of the two smallest sides is lower than the greatest side, increas the count
#     i+=1 
#     if i % 3 == 0: i +=6 # If we are at the end of a line, the next value has ever been considered previously. The next non-considerated value is the 6th afterward

# print('My bad. I misunderstood the groups specification. After update, there is', count, 'possibles rectangles.')

