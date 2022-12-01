def checksum(s,disk_length):
    while len(s) < disk_length : # Compute the checksum until it reaches the required length
        s+='0'+''.join([str(1-(int(b))) for b in s[::-1]])
    s=s[:disk_length] # Troncate such that we only have the exact required length
    while len(s) % 2 == 0 : # Reducing modulo 2
        s=''.join([str(int(t[0]==t[1])) for t in [s[i:i+2] for i in range(0,len(s),2)]])
    return s

input='11101000110010100'
print('First disk is full. Its correct checksum is', checksum('11101000110010100',272),'. Now let\'s fill the second disk')
print('Done! Its checksum is', checksum('11101000110010100',35651584))
