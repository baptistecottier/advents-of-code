from _md5 import md5

def generator(input: str): 
    return input

def part_1(door_id: str) : 
    return get_password(door_id, position = False)

def part_2(door_id: str) : 
    return get_password(door_id, position = True)


def get_password(door_id: str, position: bool):
    password: dict = {}
    index: int     = 0
    pw_index: int  = -1
    
    while len(password) < 8 :    
        hash: str = md5(f"{door_id}{index}".encode()).hexdigest()
        if hash.startswith("00000"):
            match position : 
                case True  : pw_index = int(hash[5],16)
                case False : pw_index += 1
              
            if pw_index in range(8) and pw_index not in password: 
                password[pw_index] = hash[5 + position]
                
        index = index + 1
    
    return ''.join(password[index] for index in range(8))