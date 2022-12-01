from re import I


input=open('inputs/11.txt').read().splitlines()

# This is not a general solution. The values obtained are lower bounds, and 
# if the input is well-formed, it works.

# The idea is to put all elements on the i-th floor to the (i+1)-th floor, 
# no matter if they are generators or microchip. Put an element on the next floor
# requires two steps (an elevator round-trip), except for the two last elements, 
# that reach next floor in one step.
# If we have n elements to put on the next floor, this requires 2*(n-2)+1=2*n+3 steps

# Extract number of element by floor
elements=[floor.count('microchip')+floor.count('generator') for floor in input]

elements[0]+=4 # Adding the 4 extra-elements in the first floor
print('Noooo, yet another surprise. Let\'s consider those new elements.')
print('Ok, now I need',sum(2*sum(elements[:x]) - 3 for x in range(1,4)), 'steps to build my computer')
