import re
from AoC_tools import read_input
from parse import *

programs=re.findall(r'\b[^\d\W]+\b',read_input())
for prog in programs:
    if programs.count(prog)== 1 : 
        print("The name of the bottom programme is", prog)

programs=read_input().splitlines()
nodes , weights = {} , {}

for program in programs :
    p, w, other = parse('{:l} ({:d}{}', program)
    weights[p]=w
    if '->' in other : 
        _, l = parse('{} -> {}', other)
        nodes[p]=l.split(', ') 

def add_weight(p, ns, ws):
    if p in ns : return ws[p]+sum([add_weight(tt, ns, ws) for tt in ns[p]])
    else : return ws[p]

tw=weights.copy()
for node in nodes : 
    weights[node]+=sum([add_weight(t, nodes, tw) for t in nodes[node]])

for node in nodes : 
    list_weights = [weights[item] for item in nodes[node]]
    mn , mx = min(list_weights) , max(list_weights)
    if mn != mx :
        delta = mx - mn
        if list_weights.count(mn) == 1 :
            wrong_weight_prog=nodes[node][list_weights.index(mn)]
            print(tw[wrong_weight_prog]+delta)
        else : 
            wrong_weight_prog=nodes[node][list_weights.index(mx)]
            print(tw[wrong_weight_prog]-delta)
        break