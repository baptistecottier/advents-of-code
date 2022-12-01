import collections
from decimal import DecimalException

with open("inputs/04.txt") as f: 
    rooms=f.read().splitlines()

sumID=0
real_rooms=[]

for room in rooms : 
    
    # We retrieve the informations we want
    checksum=room[-6:-1]
    roomID=int(room[-10:-7])
    room=room[:-11]

    # We count each character occurence
    count=collections.Counter(room.replace('-','')).items()
    # We sort the values:
    # First consider the opposite value of item[1] , then the alphabet rank of item[0]
    # Keep the five bests
    count=sorted(count , key = lambda item: (-item[1], item[0]))[:5]

    real_checksum=''
    for character , cnt in count : real_checksum+=character
    if real_checksum == checksum : 
        real_rooms.append([room, roomID]) # Save the room for Part II
        sumID += roomID 
print('Even if it is not a secure checksum, the sum of the sector IDs of the real rooms is', sumID)

alphabet=[chr(i) for i in range(97,123)] # Really ? It just generates an alphabet

for room,key in real_rooms: # Going throught the real rooms
    decrypted_room=''
    for c in list(room) : 
        if c=='-' : dec_c = ' '
        else :
            mod_key = (key - 97) % 26 # To anticipate the use of the function ord, we substract 97.
            dec_c=alphabet[(ord(c) + mod_key) % 26] # Gathering the decrypted characters
        decrypted_room+=dec_c
    if 'north' in decrypted_room : 
        print('Hopefully, I did the CRYPTIS master at Limoges. So I can tell you that North Pole objects \nare stored in the room','_'+ decrypted_room+'_','with sector ID', key)
        break
