from AoC_tools import read_input
intervales=read_input().splitlines()

# Extraction of the intervales
intervales=[list(map(int,intervale.split('-'))) for intervale in intervales]

# Recursive function that find the next IP that is allowed
def find_next_allowed_IP(start ,intervales):
    for inf , sup in intervales : # We go across the intervales
        if start in range(inf, sup+1) : # If the IP value is in one of the intervale
            intervales=[(inf , sup) for (inf , sup) in intervales if sup >  start] # Update the intervales 
            return find_next_allowed_IP(sup+1 ,intervales) # Recall the function with the updated candidate
    return start # If the candidate is in none of the intervales, so the IP is allowed

# Part I
i=find_next_allowed_IP(0,intervales)
print('The first allowed IP is' , str(i)+'.') 

allowed_IP=0
while i < (1 << 32) : # We now the range of IPs is 0 - 4294967295=2^32
    intervales=[(inf , sup) for (inf , sup) in intervales if sup >  i ] # Updating the intervales
    new_i=min(intervales , key = lambda item : item[0])[0] # Reaching the next intervale lower bound
    allowed_IP += new_i - i # Updating the allowed IP amount
    i = find_next_allowed_IP(new_i, intervales) # Find the next allowed value

# Part II
print('This is the first from a list of' , allowed_IP, 'IPs.')
