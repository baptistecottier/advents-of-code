def tile_type(left, right):
    if (left == right) : return '.'
    else : return '^'

input='.^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^.'

s='.'+input+'.' # We surrounds the input by dot to simulate safe tiles.
safe_tiles=s.count('.')-2 # We count the safe tiles without forgetting to substract the two sided safe tiles
for t in range(40000):
    s='.'+''.join([tile_type(s[i]=='^',s[i+2]=='^') for i in range(len(s)-2)])+'.'
    safe_tiles+=s.count('.')-2
    if t==38 : print('In a total of 40 rows, there are', safe_tiles, 'safe tiles')
print('while for a total of 40 000 rows, we have:', safe_tiles, 'safe tiles.')