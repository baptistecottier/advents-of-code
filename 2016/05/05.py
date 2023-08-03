from _md5 import md5

def parser(data): 
    return data

def solver(door_id):
    pw_m1 = ''
    pw_m2 = list('________')
    index = 0
    
    while '_' in pw_m2 :    
        hash = md5(f"{door_id}{index}".encode()).hexdigest()
        if hash.startswith("00000"):
            pw_index = int(hash[5], 16)
            if pw_index < 8 and pw_m2[pw_index] == '_':
                    pw_m2[pw_index] = hash[6]
            pw_m1 += hash[5]
        index += 1
    yield pw_m1[:8]
    yield ''.join(pw_m2)