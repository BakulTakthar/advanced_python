"""
example of iterables

    a file as an iterbale means we can iterate on each of its lines and work
    on each of them
individually

"""


# *? we are using the READLINE() method
def iteration_using_readline():
    line_num = 0

    print("\n\n\n\n code starts here \n\n\n\n")

    for line in open("sys.py"):
        line_num += 1
        print(f"{line_num} | {line}")

# iteration_using_readline() # <- run this for the above mentioned method


# *? we are using the NEXT() / __NEXT__() method
# **
# *! this method to my knowledge only seems to work with every single time
# *! you seem to run it

# *TODO see if this method works otherwise


def iteration_using_next():
    line_num = 0

    print("\n\n\n\n code starts here \n\n\n\n")

    open1 = open("sys.py")

    for line in open1:
        line_num += 1
        line = next(open1)
        print(f"{line_num} | {line}")

# iteration_using_next()   # <- run this for the above mentioned method


"""
Theory of itertators

the iteration classification of object is done on two basis 1) iteration tool and 2) iterator object

1) iteration tool/conetxt - the tools and objects or conditions which make the iteration possible in the 
'iterable object' (does itertaion on an object which allows iteration).
for example for, map, comprehension etc.

2) iterator object - the object returned by the iteration on the iterable object
(the output retured by oone itertaion on the iterable object by the iteration tool/ context)
"""

# *? sometimes the iterator object (the output object of the iteration tool/context on the iterable object) is an iterable object as well (allows for iteration)
# *? eg- itertaion on a nested list returns another list (which by being a list itself, allows for itertion) is an iterable object.

'''example code to understand better'''





def example_of_theory():
    l2 = []
    # * initialising/declaring the iterable object
    l1 = [1, 2, 3, 4, [3, 4, 5], 5, 6, 7, 8, 9, 0]
    for i in l1:  # * making the iteration tool/conetext (for in our case)

        l2.append(i)  # * declaring the iterator object

        if i is not int:  # * checking if the iterator object is iterable in# * intself
            iterable_output = i  # * placing it in a seperate variable
            l2.remove(i)
    # * printing both iterable and non iterable output objects
    print(l2, iterable_output)

# example_of_theory() # <- run this for the above mentioned method


''' checking if an object is iterable

concept -- if an object is its own iterator {returns true in the iter(-object-) is -object-}

        if an object is its own iterator then it will only support one itertion at a time
         (will not support multiple iterations at a time eg- both itertions when one is going 
         forward and one is going backwards at the same time.)
         example - a file   
concept -- if an object is not its own iterator {returns false in the iter(-object-) is -object-}
        same but will support two way or even n-way iteration
'''


def checking_iterability():
    f = open('sys.py')
    print(f"{iter(f) is f} | true because it is a file")

    g = [1, 2, 3, 4, 5, 6, 7]
    print(f"{iter(g) is g} | false because it is a list")

# checking_iterability()  # <- run this for the above mentioned method


""" enumerate objects are iterable too"""


def enumerate_iteration():
    E = enumerate("bakul")

    I = iter(E)
    output = []
    for i in I:
        output.append(i)
    print(output)


# enumerate_iteration()   # <- run this for the above mentioned method

'''list comprehension'''


def list_comprehension():
    L = [1, 2, 3, 4, 5, 6,]

    for i in range(len(L)):
        L[i] += 10
    print(L)
    '''list comprehensions are written in squary braces just like lists
    but comatain instruction on an existing list to iterate and modify it'''

    L = [X + 10 for X in L]     # example of list comprehension
    print(L)
# list_comprehension()  # <- run this for the above mentioned method


def list_comprehension_on_file():
    file = open('sys.py')

    lines = file.readlines()
    print(lines)
    print('\n\n')
    '''list comprehension on files by modifying the layout or results'''

    lines = [line.rstrip() for line in lines]
    print(lines)
    print('\n\n')
    '''using conditional statements on the '''
    lines = [line.rstrip() for line in lines if len(lines)]
    print(lines)
    print('\n\n')
    '''using nested for loops in list comprehension'''
    list = [x + y for x in 'abc' for y in '123']
    print(list)

# list_comprehension_on_file() # <- run this for the above mentioned method


'''list comprehension is way better than employing complete for loops to do basic iteration on lists
because its less lines of code and can be 2 times as fast as the standard method of creating an entirely 
seperate for loop '''
