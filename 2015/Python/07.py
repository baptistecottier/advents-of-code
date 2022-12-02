def myord(string):
    c=0
    for char in string:
        c*=26
        c+=ord(char)-96
    return c-1

wires=[-1 for col in range(myord('zz'))] 
print(wires)
with open("Day7/input.txt") as f: 
    instructions=f.read().splitlines()
    done=[]
    i=0
    while (len(done)!=len(instructions)):
        print(len(done))
        i=i%len(instructions)
        if instructions[i] not in done:
            inputs, output = instructions[i].split(' -> ')
            input=inputs.split(' ')    
            if len(input)==1:
                if input[0].isdigit():
                    wires[myord(output)]=int(input[0])
                    done.append(instructions[i])

                elif wires[myord(input[0])] != -1 : 
                    wires[myord(output)]=wires[myord(input[0])]
                    done.append(instructions[i])
                
            elif len(input)==2 and (wires[myord(input[1])] != -1) : 
                wires[myord(output)] = ~ wires[myord(input[1])] % 2**16
                done.append(instructions[i])

            elif len(input)==3 :
                if (not input[2].isdigit()) and (not input[2].isdigit()) and (wires[myord(input[0])] != -1 ) and  (wires[myord(input[2])] != -1 ) : 
                    if input[1]=='AND': wires[myord(output)]=(wires[myord(input[0])] & wires[myord(input[2])]) % 2**16
                    elif input[1]=='OR': wires[myord(output)]=(wires[myord(input[0])] | wires[myord(input[2])]) % 2**16
                    elif input[1]=='LSHIFT': wires[myord(output)]= (wires[myord(input[0])] << int(input[2])) % 2**16
                    elif input[1]=='RSHIFT': wires[myord(output)]=(wires[myord(input[0])] >> int(input[2])) % 2**16
                    done.append(instructions[i])
               
                elif (wires[myord(input[0])] != -1 ) and  (input[2].isdigit()) : 
                    if input[1]=='AND': wires[myord(output)]=(wires[myord(input[0])] & int(input[2])) % 2**16
                    elif input[1]=='OR': wires[myord(output)]=(wires[myord(input[0])] | int(input[2])) % 2**16
                    elif input[1]=='LSHIFT': wires[myord(output)]= (wires[myord(input[0])] << int(input[2])) % 2**16
                    elif input[1]=='RSHIFT': wires[myord(output)]=(wires[myord(input[0])] >> int(input[2])) % 2**16
                    done.append(instructions[i])

                elif (not input[2].isdigit()) and (wires[myord(input[2])] != -1 ) and  (input[0].isdigit()) : 
                    if input[1]=='AND': wires[myord(output)]=(wires[myord(input[2])] & int(input[0])) % 2**16
                    elif input[1]=='OR': wires[myord(output)]=(wires[myord(input[2])] | int(input[0])) % 2**16
                    elif input[1]=='LSHIFT': wires[myord(output)]= (wires[myord(input[2])] << int(input[0])) % 2**16
                    elif input[1]=='RSHIFT': wires[myord(output)]=(wires[myord(input[2])] >> int(input[0])) % 2**16
                    done.append(instructions[i])
        i += 1            
print(wires[myord('a')])