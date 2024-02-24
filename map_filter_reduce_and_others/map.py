'''
#? to get a grasp of map() function in python
'''

example = [1,2,3,4,5,6,7,8,9,10]

'''
#*- lets say that we need to add one to each of the element of this list
'''
#* without map() function

for i in range(len(example)):
    example[i] = example[i] + 1
    
print(example)

#* WITH THE MAP FUNCTION
example = map(lambda x: x + 1, example)
print(list(example))