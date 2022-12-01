from AoC_tools import read_input

passphrases=read_input().split('\n')

score1, score2 = 0,0
for passphrase in passphrases:
    score1 += not any([passphrase.count(word)>1 for word in passphrase.split(' ')])
    passphrase=[''.join(sorted(p)) for p in passphrase.split(' ')]
    score2 += not any([passphrase.count(word)>1 for word in passphrase])


print(score1, score2)
