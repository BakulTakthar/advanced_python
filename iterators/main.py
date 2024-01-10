"""
example of iterables 

    a file as an iterbale means we can iterate on each of its lines and work on each of them
individually

"""


#*? we are using the READLINE() method
def iteration_using_readline():
    line_num = 0

    print("\n\n\n\n code starts here \n\n\n\n")

    for line in open("sys.py"):
        line_num += 1
        print(f"{line_num} | {line}")

# iteration_using_readline() # <- run this for the above mentioned method


#*? we are using the NEXT() / __NEXT__() method
                    #**
                    #*! this method to my knowledge only seems to work with every single time 
                    #*! you seem to run it

                    #*TODO see if this method works otherwise


def iteration_using_next():
    line_num = 0

    print("\n\n\n\n code starts here \n\n\n\n")
    
    open1 = open("sys.py")

    for line in open1:
        line_num += 1
        line = next(open1)
        print(f"{line_num} | {line}")

#iteration_using_next()   # <- run this for the above mentioned method
        
"""
Theory of itertators 

the iteration classification of object is done on two basis 1) iteration tool and 2) iterator object

1) iteration tool/conetxt - the tools and objects or conditions which make the iteration possible in the 
'iterable object' (does itertaion on an object which allows iteration).
for example for, map, comprehension etc.

2) iterator object - the object returned by the iteration on the iterable object
(the output retured by oone itertaion on the iterable object by the iteration tool/ context)
"""

#*? sometimes the iterator object (the output object of the iteration tool/context on the iterable object) is an iterable object as well (allows for iteration)
#*? eg- itertaion on a nested list returns another list (which by being a list itself, allows for itertion) is an iterable object.