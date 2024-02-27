array = ['a', 'e', 'i', 'o', 'u']

alphabets = ['a', 'b', 'c', 'd', 'e']

result = filter(lambda x: x in array, alphabets)
print(list(result))