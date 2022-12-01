modules=open("day1.txt").read().splitlines()
total=0
for module in modules:
    fuel=int(int(module) / 3) - 2
    total_fuel=0
    #Comment section below for part one
    while fuel>0 :
        total_fuel=total_fuel+fuel
        fuel=int(fuel / 3) - 2
    total=total+total_fuel
print(total)
#up to here
#print(fuel)