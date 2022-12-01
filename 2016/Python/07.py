import re

with open("inputs/07.txt") as input:
    IPs=input.read().splitlines()

# Function detecting if 'ABBA' pattern is in a string s
def ABBA(s):
    if any([s[i:i+2]==s[i+2:i+4][::-1] and s[i] != s[i+1] for i in range(len(s)-3)]) : # If an ABBA pattern appears
        hypernet = re.findall(r'\[[\w]*\]',s) # Extract hypernets
        for h in hypernet :
            if ABBA(h[1:-1]) : return 0 # If an ABBA sequence is detectd among the hypernet, return 0
        return 1
    return 0

valid = sum([ABBA(IP) for IP in IPs])
print('There is', valid, 'IPs that support TLS')


# Function looking for ABA patterns in hypernets. For any ABA pattern found, append BAB to the list
def list_BAB_hypernet(input):
    list_ABA=[]
    for s in re.findall(r'\[[\w]*\]',input) : # Extract hypernets
        for i in range(len(s)-2): # Check for ABA patterns
            if s[i]==s[i+2] and s[i] != s[i+1] : list_ABA.append(s[i+1]+s[i]+s[i+1])
    return list_ABA


valid=0
for IP in IPs:
    wohIP= re.sub(r'\[[\w]*\]','',IP) # Substract hypernets from IPs 
    for pattern in list_BAB_hypernet(IP): # Check if any BAB pattern occurs in the resulting IP
        if pattern in wohIP : 
            valid += 1
            break

# valid=sum([any([x in re.sub(r'\[[\w]*\]','',IP) for x in list_BAB_hypernet(IP)]) for IP in IPs]) # One line equivalent
print('and', valid, 'IPs that support SSL')