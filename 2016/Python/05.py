import hashlib

input='abbhdwsy'
password_1,password_2='', list('________')

i=0
while any([item == '_' for item in password_2]): 
    hash=hashlib.md5((input+str(i)).encode()).hexdigest() # New hash computation
    if hash[:5]=='00000': # If the first five characters are zeros, fill respectives passwords
        if len(password_1)<8 : password_1 +=hash[5] 
        if 0<=int(hash[5],16)<8 and password_2[int(hash[5],16)]== '_' : password_2[int(hash[5])]=hash[6] 
    i+=1
    
print('It seems that the password is', password_1, 'but it does not work...')
print('Oh! Got it. Let\'s try',''.join(password_2), 'instead. It works!!!')