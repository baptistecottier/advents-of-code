import hashlib

def generator(input): return input

def part_1(input) : return solver(input, position = False)

def part_2(input) : return solver(input, position = True)


def solver(input, position):
    password, index, pw_index = list('________'), -1, -1
    
    while '_' in password :    
        index += 1
        hash=hashlib.md5((input+str(index)).encode()).hexdigest()
        if hash[:5]=='00000':
            match position : 
                case True : pw_index = int(hash[5],16)
                case False : pw_index += 1
              
            if pw_index in range(8) and password[pw_index] == '_' : password[pw_index] = hash[5+position]
    
    return ''.join(password )