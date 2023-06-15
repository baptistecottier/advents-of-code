import sys
import AoC_tools

sys.path.append("../"+sys.argv[1][:2])
module = __import__(sys.argv[1])



if len(sys.argv) == 3: path='../'+sys.argv[1][:2]+'/'+sys.argv[1][:2]+'_'+sys.argv[2]+'.txt'
else: path='../'+sys.argv[1][:2]+'/'+sys.argv[1][:2]+'.txt'
input_file=open(path, "r").read()


input = module.generator(input_file) 
print(module.part_1(input))
print(module.part_2(input))