"""
example of iterables 

    a file as an iterbale means we can iterate on each of its lines and work on each of them
individually

"""


''' we are using the READLINE() method'''
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

iteration_using_next()