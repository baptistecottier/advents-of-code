from asyncore import read
from AoC_tools import read_input
import re
banks = [int(item) for item in re.findall(r'\d+',read_input())]
nb_bank=len(banks)
list_banks=[]
while banks not in list_banks:
    list_banks.append(banks.copy())
    
    max_blocks=max(banks)
    max_blocks_index=banks.index(max_blocks)
    banks[max_blocks_index]=0
    for i in range(nb_bank) : banks[i]+= max_blocks // nb_bank
    for i in range(max_blocks % nb_bank) : banks[(max_blocks_index+i+1) % nb_bank] += 1
print(len(list_banks)-list_banks.index(banks))