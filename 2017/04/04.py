def preprocessing(data):
    return [passphrase.split(' ') for passphrase in data.splitlines()]

def solver(passphrases):
    yield sum(len(set(passphrase)) == len(passphrase) for passphrase in passphrases)
    yield sum(len(set(''.join(sorted(p)) for p in passphrase)) == len(passphrase) for passphrase in passphrases)
