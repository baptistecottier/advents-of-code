def preprocessing(data):
    return (passphrase.split(' ') for passphrase in data.splitlines())


def solver(passphrases):
    valid       = 0
    safer_valid = 0
    
    for passphrase in passphrases:
        if len(passphrase) == len(set(passphrase)): 
            valid += 1
            if len(set(''.join(sorted(p)) for p in passphrase)) == len(passphrase):
                safer_valid += 1
                
    yield valid
    yield safer_valid