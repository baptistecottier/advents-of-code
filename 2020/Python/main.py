import sys

module = __import__(sys.argv[1])
input_file=open('../inputs/'+sys.argv[1]+'.txt', "r").read()


input = module.generator(input_file) 
print(module.part_1(input))
print(module.part_2(input))