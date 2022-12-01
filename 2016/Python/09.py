from parse import parse

with open("inputs/09.txt") as f: 
    input = f.read()


def decompress(s, part):
    if '(' not in s : return len(s) # No parenthesis implies no decompression needed. The input string is the final string
    i=0
    while i<len(s):
        if s[i]=='(': #Detecting decompression instruction
            instructions, _ = parse('({}){}',s[i:]) # Extract instructions
            length , time = parse('{:d}x{:d}',instructions) # Extract settings of the instruction
        
            if part==1: # For part I, we have to ignore the decompression instructions inside a decompression
                return i + time * length + decompress(s[i+len(instructions)+2+length:], part)

            if part==2: # For part II, we have to consider the decompression instructions inside a decompression
                return i + time * decompress(s[i+len(instructions)+2:i+len(instructions)+2+length],part) + decompress(s[i+len(instructions)+2+length:], part)
        
        else : i+=1

print('The decompressed size of the file is', decompress(input,1), 'but that seems too few...')
print('Oh, once again I forget to update my mind, I had to use the version 2.')
print('This results in a decompressed length of', decompress(input,2))