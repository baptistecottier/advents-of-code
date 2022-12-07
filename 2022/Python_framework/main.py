import sys

sys.path.append("../"+sys.argv[1])
module = __import__(sys.argv[1])


path='../'+sys.argv[1]+'/'+sys.argv[1]+'.txt'
input_file=open(path, "r").read()


input = module.generator(input_file) 
print(module.part_1(input))
print(module.part_2(input))