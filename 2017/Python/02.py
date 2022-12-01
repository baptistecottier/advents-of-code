from AoC_tools import read_input

spreadsheet=read_input().splitlines()
spreadsheet=[list(map(int,line.split('\t'))) for line in spreadsheet]
checksum_1=sum([max(line)-min(line) for line in spreadsheet])

checksum_2=0
for line in spreadsheet:
    for n in line : 
        for t in line : 
            if n % t == 0 and n != t : checksum_2 += n//t
print('The checksum of the spreadsheet is ' +str(checksum_1) +'. What do you mean ? That\'s not the way to do it ? Ok, so what about', checksum_2,'?')
