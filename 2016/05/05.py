from _md5 import md5

def parser(data: str): 
    return data

def solver(door_id: str):
    pw_m1: str  = ''
    pw_m2: list = list('________')
    index: int  = 0
    
    while '_' in pw_m2 :    
        hash: str = md5(f"{door_id}{index}".encode()).hexdigest()
        if hash.startswith("00000"):
            pw_index = int(hash[5],16)
            if pw_index < 8 and pw_m2[pw_index] == '_':
                    pw_m2[pw_index] = hash[6]
            pw_m1 += hash[5]
        index += 1
    yield pw_m1[:8]
    yield ''.join(pw_m2)