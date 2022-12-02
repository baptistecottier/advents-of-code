import sys

module = __import__(sys.argv[1])

path='../inputs/'+sys.argv[1]+'.txt'
input_file=open(path, "r").read()


input = module.generator(input_file) 
print(module.part_1(input))
print(module.part_2(input))